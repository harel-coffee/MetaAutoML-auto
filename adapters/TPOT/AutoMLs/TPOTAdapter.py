
from AdapterUtils import *
from AdapterTabularUtils import *
from tpot import TPOTClassifier, TPOTRegressor


class TPOTAdapter:
    """
    Implementation of the AutoML functionality for TPOT
    """

    def __init__(self, configuration: dict):
        """Init a new instance of TPOTAdapter

        Args:
            configuration (dict): Dictonary holding the training configuration
        """
        self._configuration = configuration

    def start(self):
        """
        Start the correct ML task functionality of TPOT
        """
        if True:
            if self._configuration["configuration"]["task"] == ":tabular_classification":
                self.__tabular_classification()
            elif self._configuration["configuration"]["task"] == ":tabular_regression":
                self.__tabular_regression()

    def __tabular_classification(self):
        train, test = data_loader(self._configuration, perform_splitting=False)
        X, y = prepare_tabular_dataset(train, self._configuration)
        #Apply encoding to string
        self._configuration = set_encoding_for_string_columns(self._configuration, X, y, also_categorical=True)
        self._configuration = set_imputation_for_numerical_columns(self._configuration, X)
        train, test = data_loader(self._configuration)
        #reload dataset to load changed data
        X, y = prepare_tabular_dataset(train, self._configuration)
        pipeline_optimizer = TPOTClassifier(generations=1, population_size=2, cv=5,
                                            random_state=42, verbosity=2, max_time_mins=self._configuration["configuration"]["runtime_limit"]*60)
        pipeline_optimizer.fit(X, y)
        export_model(pipeline_optimizer.fitted_pipeline_, self._configuration["result_folder_location"], 'model_TPOT.p')


    def __tabular_regression(self):
        train, test = data_loader(self._configuration, perform_splitting=False)
        X, y = prepare_tabular_dataset(train, self._configuration)
        #Apply encoding to string
        self._configuration = set_encoding_for_string_columns(self._configuration, X, y, also_categorical=True)
        self._configuration = set_imputation_for_numerical_columns(self._configuration, X)
        train, test = data_loader(self._configuration)
        #reload dataset to load changed data
        X, y = prepare_tabular_dataset(train, self._configuration)

        pipeline_optimizer = TPOTRegressor(generations=5, population_size=5, cv=5,
                                            random_state=42, verbosity=2, max_time_mins=self._configuration["configuration"]["runtime_limit"]*60)
        pipeline_optimizer.fit(X, y)
        export_model(pipeline_optimizer.fitted_pipeline_, self._configuration["result_folder_location"], 'model_TPOT.p')