import functools
import os
import shutil

import adanet
import tensorflow.compat.v1 as tf

# The random seed to use.
RANDOM_SEED = 42

LOG_DIR = '/tmp/models'
FEATURES_KEY = "x"


def input_fn(partition, training, batch_size):
  """Generate an input function for the Estimator."""

  def _input_fn():

    if partition == "train":
      dataset = tf.data.Dataset.from_tensor_slices(({
          FEATURES_KEY: tf.log1p(x_train)
      }, tf.log1p(y_train)))
    else:
      dataset = tf.data.Dataset.from_tensor_slices(({
          FEATURES_KEY: tf.log1p(x_test)
      }, tf.log1p(y_test)))

    # We call repeat after shuffling, rather than before, to prevent separate
    # epochs from blending together.
    if training:
      dataset = dataset.shuffle(10 * batch_size, seed=RANDOM_SEED).repeat()

    dataset = dataset.batch(batch_size)
    iterator = dataset.make_one_shot_iterator()
    features, labels = iterator.get_next()
    return features, labels

  return _input_fn

#@title AdaNet parameters
LEARNING_RATE = 0.001  #@param {type:"number"}
TRAIN_STEPS = 60000  #@param {type:"integer"}
BATCH_SIZE = 32  #@param {type:"integer"}

LEARN_MIXTURE_WEIGHTS = False  #@param {type:"boolean"}
ADANET_LAMBDA = 0  #@param {type:"number"}
ADANET_ITERATIONS = 3  #@param {type:"integer"}
_NUM_LAYERS_KEY = "num_layers"


class _SimpleDNNBuilder(adanet.subnetwork.Builder):
  """Builds a DNN subnetwork for AdaNet."""

  def __init__(self, optimizer, layer_size, num_layers, learn_mixture_weights,
               seed):
    """Initializes a `_DNNBuilder`.

    Args:
      optimizer: An `Optimizer` instance for training both the subnetwork and
        the mixture weights.
      layer_size: The number of nodes to output at each hidden layer.
      num_layers: The number of hidden layers.
      learn_mixture_weights: Whether to solve a learning problem to find the
        best mixture weights, or use their default value according to the
        mixture weight type. When `False`, the subnetworks will return a no_op
        for the mixture weight train op.
      seed: A random seed.

    Returns:
      An instance of `_SimpleDNNBuilder`.
    """

    self._optimizer = optimizer
    self._layer_size = layer_size
    self._num_layers = num_layers
    self._learn_mixture_weights = learn_mixture_weights
    self._seed = seed

  def build_subnetwork(self,
                       features,
                       logits_dimension,
                       training,
                       iteration_step,
                       summary,
                       previous_ensemble=None):
    """See `adanet.subnetwork.Builder`."""

    input_layer = tf.to_float(features[FEATURES_KEY])
    kernel_initializer = tf.glorot_uniform_initializer(seed=self._seed)
    last_layer = input_layer
    for _ in range(self._num_layers):
      last_layer = tf.layers.dense(
          last_layer,
          units=self._layer_size,
          activation=tf.nn.relu,
          kernel_initializer=kernel_initializer)
    logits = tf.layers.dense(
        last_layer,
        units=logits_dimension,
        kernel_initializer=kernel_initializer)

    shared = {_NUM_LAYERS_KEY: self._num_layers}
    return adanet.Subnetwork(
        last_layer=last_layer,
        logits=logits,
        complexity=self._measure_complexity(),
        shared=shared)

  def _measure_complexity(self):
    """Approximates Rademacher complexity as the square-root of the depth."""
    return tf.sqrt(tf.to_float(self._num_layers))

  def build_subnetwork_train_op(self, subnetwork, loss, var_list, labels,
                                iteration_step, summary, previous_ensemble):
    """See `adanet.subnetwork.Builder`."""
    return self._optimizer.minimize(loss=loss, var_list=var_list)

  @property
  def name(self):
    """See `adanet.subnetwork.Builder`."""

    if self._num_layers == 0:
      # A DNN with no hidden layers is a linear model.
      return "linear"
    return "{}_layer_dnn".format(self._num_layers)


class SimpleDNNGenerator(adanet.subnetwork.Generator):
  """Generates a two DNN subnetworks at each iteration.

  The first DNN has an identical shape to the most recently added subnetwork
  in `previous_ensemble`. The second has the same shape plus one more dense
  layer on top. This is similar to the adaptive network presented in Figure 2 of
  [Cortes et al. ICML 2017](https://arxiv.org/abs/1607.01097), without the
  connections to hidden layers of networks from previous iterations.
  """

  def __init__(self,
               optimizer,
               layer_size=64,
               learn_mixture_weights=False,
               seed=None):
    """Initializes a DNN `Generator`.

    Args:
      optimizer: An `Optimizer` instance for training both the subnetwork and
        the mixture weights.
      layer_size: Number of nodes in each hidden layer of the subnetwork
        candidates. Note that this parameter is ignored in a DNN with no hidden
        layers.
      learn_mixture_weights: Whether to solve a learning problem to find the
        best mixture weights, or use their default value according to the
        mixture weight type. When `False`, the subnetworks will return a no_op
        for the mixture weight train op.
      seed: A random seed.

    Returns:
      An instance of `Generator`.
    """

    self._seed = seed
    self._dnn_builder_fn = functools.partial(
        _SimpleDNNBuilder,
        optimizer=optimizer,
        layer_size=layer_size,
        learn_mixture_weights=learn_mixture_weights)

  def generate_candidates(self, previous_ensemble, iteration_number,
                          previous_ensemble_reports, all_reports):
    """See `adanet.subnetwork.Generator`."""

    num_layers = 0
    seed = self._seed
    if previous_ensemble:
      num_layers = previous_ensemble.subnetworks[-1].shared[_NUM_LAYERS_KEY]
    if seed is not None:
      seed += iteration_number
    return [
        self._dnn_builder_fn(num_layers=num_layers, seed=seed),
        self._dnn_builder_fn(num_layers=num_layers + 1, seed=seed),
    ]

def train_and_evaluate(experiment_name, learn_mixture_weights=LEARN_MIXTURE_WEIGHTS,
                       adanet_lambda=ADANET_LAMBDA):
  """Trains an `adanet.Estimator` to predict housing prices."""

  model_dir = os.path.join(LOG_DIR, experiment_name)

  ensembler_optimizer = None
  if learn_mixture_weights:
    ensembler_optimizer = tf.train.RMSPropOptimizer(
        learning_rate=LEARNING_RATE)

  estimator = adanet.Estimator(
      # Since we are predicting housing prices, we'll use a regression
      # head that optimizes for MSE.
      head=tf.estimator.RegressionHead(),

      # Define the generator, which defines our search space of subnetworks
      # to train as candidates to add to the final AdaNet model.
      subnetwork_generator=SimpleDNNGenerator(
          optimizer=tf.train.RMSPropOptimizer(learning_rate=LEARNING_RATE),
          learn_mixture_weights=learn_mixture_weights,
          seed=RANDOM_SEED),

      # The number of train steps per iteration.
      max_iteration_steps=TRAIN_STEPS // ADANET_ITERATIONS,

      # The evaluator will evaluate the model on the full training set to
      # compute the overall AdaNet loss (train loss + complexity
      # regularization) to select the best candidate to include in the
      # final AdaNet model.
      evaluator=adanet.Evaluator(
          input_fn=input_fn("train", training=False, batch_size=BATCH_SIZE)),

      ensemblers=[
          adanet.ensemble.ComplexityRegularizedEnsembler(
              optimizer=ensembler_optimizer,
              # Lambda is a the strength of complexity regularization. A larger
              # value will penalize more complex subnetworks.
              adanet_lambda=adanet_lambda),
      ],      

      # Configuration for Estimators.
      config=tf.estimator.RunConfig(
          save_summary_steps=5000,
          save_checkpoints_steps=5000,
          tf_random_seed=RANDOM_SEED,
          model_dir='C:\\Users\\hda10126\\Desktop\\Auto-PyTorch-master'))

  # Train and evaluate using using the tf.estimator tooling.
  train_spec = tf.estimator.TrainSpec(
      input_fn=input_fn("train", training=True, batch_size=BATCH_SIZE),
      max_steps=TRAIN_STEPS)
  eval_spec = tf.estimator.EvalSpec(
      input_fn=input_fn("test", training=False, batch_size=BATCH_SIZE),
      steps=None,
      start_delay_secs=1,
      throttle_secs=30,
  )
  tf.estimator.train_and_evaluate(estimator, train_spec, eval_spec)
  return estimator.evaluate(
      input_fn("test", training=False, batch_size=BATCH_SIZE),
      steps=None)

def ensemble_architecture(result):
  """Extracts the ensemble architecture from evaluation results."""

  architecture = result["architecture/adanet/ensembles"]
  # The architecture is a serialized Summary proto for TensorBoard.
  summary_proto = tf.summary.Summary.FromString(architecture)
  return summary_proto.value[0].tensor.string_val[0]

if __name__ == '__main__':
    (x_train, y_train), (x_test, y_test) = (tf.keras.datasets.boston_housing.load_data())

    # Preview the first example from the training data
    print('Model inputs: %s \n' % x_train[0])
    print('Model output (house price): $%s ' % (y_train[0] * 1000))
    results = train_and_evaluate("uniform_average_ensemble_baseline")
    print("Loss:", results["average_loss"])
    print("Architecture:", ensemble_architecture(results))











    phishing_dataset = pd.read_csv("C:/Users/hda10126/Desktop/titanic-dataset/phishing.csv", quotechar='"', skipinitialspace=True)
    y = phishing_dataset.Result
    x = phishing_dataset.drop('Result', axis=1)
	
	
	
	
	
	#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
	#college_dataset = pd.read_csv("C:/Users/hda10126/Desktop/titanic-dataset/college.csv", quotechar='"', skipinitialspace=True)
	#y = college_dataset.percent_pell_grant
	#x = college_dataset.drop('Result', axis=1)
	#clf = ak.StructuredDataClassifier(overwrite=True, 
	#							   max_trials=3, 
	#							   seed=42,
	#							   objective=kt.Objective('val_f1_score', direction='min'),
	#							   metrics=[f1_score])
	
    clf = ak.StructuredDataClassifier(overwrite=True, 
								   max_trials=1, 
								   seed=42,
								   objective=kt.Objective('val_f1_score', direction='max'),
								   metrics=[f1_score])
	#xlf = ak.StructuredDataRegressor(overwrite=True, 
	#							   max_trials=1, 
	#							   seed=42,
	#							   metrics=[root_mean_squared_error])
    #result = clf.fit(x, y, epochs=1)
	#print(result)
	#model = clf.export_model(custom_objects={'f1_score': f1_score})
	# Evaluate on the testing data.
	#print('Accuracy: {accuracy}'.format(
	#	accuracy=clf.evaluate(x_test, y_test)))
	#model = clf.export_model(custom_objects={'f1_score': f1_score})
	#model.summary()



	#clf = ak.StructuredDataClassifier(overwrite=True, max_trials=3, seed=42)
	#clf.fit("C:/Users/hda10126/Desktop/titanic-dataset/phishing.csv", "Result", epochs=10)
	#result = clf.predict(x_to_predict_numpy.astype(np.unicode))
	#print(result)
	#model = clf.export_model()
	#model.summary()
	#model.save("model_autokeras", save_format="tf")
	#loaded_model = load_model("model_autokeras", custom_objects=ak.CUSTOM_OBJECTS)
	#loaded_model.summary()
	#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	#for root, dirs, files in os.walk(BASE_DIR, topdown = False):
	#	for name in files:
			#print(os.path.join(root, name))

	#predicted_y = loaded_model.predict(x_to_predict_numpy.astype(np.unicode))
	#predicted_y[predicted_y < 0.5] = 0
	#predicted_y[predicted_y > 0.5] = 1