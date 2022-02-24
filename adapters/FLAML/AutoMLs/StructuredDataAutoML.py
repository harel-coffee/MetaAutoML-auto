import os
import pandas as pd
import pickle
from flaml import AutoML

from Utils.JsonUtil import get_config_property
from AutoMLs.predict_time_sources import feature_preparation, DataType, SplitMethod

class StructuredDataAutoML(object):
    """
    Implementation of the AutoML functionality fo structured data a.k.a. tabular data
    """

    def __init__(self, configuration: dict):
        """
        Init a new instance of StructuredDataAutoML
        ---
        Parameter:
        1. Configuration JSON of type dictionary
        """
        self.__configuration = configuration

    def __read_training_data(self):
        """
        Read the training dataset from disk
        """
        df = pd.read_csv(os.path.join(self.__configuration["file_location"], self.__configuration["file_name"]),
                         **self.__configuration["file_configuration"])

        # split training set
        if SplitMethod.SPLIT_METHOD_RANDOM == self.__configuration["test_configuration"]["method"]:
            df = df.sample(random_state=self.__configuration["test_configuration"]["random_state"], frac=1)
        else:
            df = df.iloc[:int(df.shape[0] * self.__configuration["test_configuration"]["split_ratio"])]

        target = self.__configuration["tabular_configuration"]["target"]["target"]
        self.__X = df.drop(target, axis=1)
        self.__y = df[target]

    def __dataset_preparation(self):
        feature_preparation(self.__X, self.__configuration["tabular_configuration"]["features"].items())
        self.__cast_target()

    def __cast_target(self):
        target_dt = self.__configuration["tabular_configuration"]["target"]["type"]
        if DataType(target_dt) is DataType.DATATYPE_CATEGORY:
            self.__y = self.__y.astype('category')
        elif DataType(target_dt) is DataType.DATATYPE_BOOLEAN:
            self.__y = self.__y.astype('bool')
        elif DataType(target_dt) is DataType.DATATYPE_INT:
            self.__y = self.__y.astype('int')
        elif DataType(target_dt) is DataType.DATATYPE_FLOAT:
            self.__y = self.__y.astype('float')

    def __export_model(self, model):
        """
        Export the generated ML model to disk
        ---
        Parameter:
        1. generate ML model
        """
        with open(os.path.join(get_config_property('output-path'), 'tmp', 'model_flaml.p'), 'wb+') as file:
            pickle.dump(model, file)

    def execute_task(self):
        """
        Execute the ML task
        """
        if self.__configuration["task"] == 1:
            self.__classification()
        elif self.__configuration["task"] == 2:
            self.__regression()

    def __generate_settings(self):
        automl_settings = {"log_file_name": 'flaml.log'}
        if self.__configuration["runtime_constraints"]["runtime_limit"] != 0:
            automl_settings.update({"time_budget": self.__configuration["runtime_constraints"]["runtime_limit"]})
        if self.__configuration["runtime_constraints"]["max_iter"] != 0:
            automl_settings.update({"max_iter": self.__configuration["runtime_constraints"]["max_iter"]})
        return automl_settings

    def __classification(self):
        """
        Execute the classification task
        """
        self.__read_training_data()
        self.__dataset_preparation()
        automl = AutoML()
        automl_settings = self.__generate_settings()
        automl_settings.update({
            "metric": self.__configuration["metric"] if self.__configuration["metric"] != "" else 'accuracy',
            "task": 'classification',
        })

        automl.fit(X_train=self.__X, y_train=self.__y, **automl_settings)
        self.__export_model(automl)

    def __regression(self):
        """
        Execute the regression task
        """
        self.__read_training_data()
        self.__dataset_preparation()
        automl = AutoML()
        automl_settings = self.__generate_settings()
        automl_settings.update({
            "metric": self.__configuration["metric"] if self.__configuration["metric"] != "" else 'rmse',
            "task": 'regression',
        })

        automl.fit(X_train=self.__X, y_train=self.__y, **automl_settings)
        self.__export_model(automl)
