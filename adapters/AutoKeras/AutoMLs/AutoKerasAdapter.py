import os
import dill
import pandas as pd
import autokeras as ak

from enum import Enum, unique
from JsonUtil import get_config_property
from predict_time_sources import feature_preparation, DataType, SplitMethod 
from AbstractAdapter import AbstractAdapter
from AdapterUtils import read_tabular_dataset_training_data, prepare_tabular_dataset

class AutoKerasAdapter(AbstractAdapter):
    """
    Implementation of the AutoML functionality for AutoKeras
    """
    def __init__(self, configuration: dict):
        """
        Init a new instance of AutoKerasAdapter
        ---
        Parameter:
        1. Configuration JSON of type dictionary
        """
        super(AutoKerasAdapter, self).__init__(configuration)

    def start(self):
        """Execute the ML task"""
        if True:
            if self._configuration["task"] == 1:
                self.__tabular_classification()
            elif self._configuration["task"] == 2:
                self.__tabular_regression()

    def __export_model(self, model):
        """
        Export the generated ML model to disk
        ---
        Parameter:
        1. generate ML model
        """
        with open(os.path.join(get_config_property('output-path'), 'tmp', 'model_keras.p'), 'wb+') as file:
            dill.dump(model, file)

    def __tabular_classification(self):
        """Execute the classification task"""
        self.df = read_tabular_dataset_training_data(self._configuration)
        X, y = prepare_tabular_dataset(self.df, self._configuration)
        clf = ak.StructuredDataClassifier(overwrite=True,
                                          max_trials=self._max_iter,
                                          # metric=self._configuration['metric'],
                                          seed=42)
                                          
        clf.fit(x=X, y=y)
        self.__export_model(clf)

    def __tabular_regression(self):
        """Execute the regression task"""
        read_tabular_dataset_training_data(self._configuration)
        prepare_tabular_dataset(self._configuration)
        reg = ak.StructuredDataRegressor(overwrite=True,
                                         max_trials=self._max_iter,
                                         # metric=self._configuration['metric'],
                                         seed=42)
        reg.fit(x=self._X, y=self._y)
        self.__export_model(reg)
