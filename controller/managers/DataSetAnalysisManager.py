from typing import Dict
import pandas as pd
import numpy as np
import json

class DataSetAnalysisManager:
    """
    Static DataSetAnalysisManager class to analyze the dataset
    """
    
    def startAnalysis(dataset: pd.DataFrame):
        """
        Initialization of the analysis, results are written to JSON file
        ---
        Parameter
        1. dataset to be analyzed
        ---
        Return None
        """
        jsonfile = {}
        jsonfile["basic analysis"] = {}
        jsonfile = DataSetAnalysisManager.__number_of_rows_and_columns(dataset, jsonfile)
        jsonfile = DataSetAnalysisManager.__missing_values(dataset, jsonfile)
        jsonfile = DataSetAnalysisManager.__detect_outliers(dataset, jsonfile)

        # print(json.dumps(jsonfile))

        with open('controller\app-data\analysis.json', 'w+') as target:
            json.dump(jsonfile, target)
        
    @staticmethod
    def __number_of_rows_and_columns(dataset: pd.DataFrame, jsonfile: dict) -> dict:
        """
        Counts the number of rows and columns of the dataset and adds that information to a JSON file
        ---
        Parameter
        1. dataset to be analyzed
        2. JSON file to write to
        ---
        Return the JSON file with additional data
        """
        rows, columns = dataset.shape

        jsonfile["basic analysis"]["number of rows"] = rows
        jsonfile["basic analysis"]["number of columns"] = columns

        return jsonfile

    @staticmethod
    def __missing_values(dataset: pd.DataFrame, jsonfile: dict) -> dict:
        """
        Counts missing values of each column and row and adds that information to a JSON file
        ---
        Parameter
        1. dataset to be analyzed
        2. JSON file to write to
        ---
        Return the JSON file with additional data
        """

        jsonfile["basic analysis"]["missing values in columns"] = {}
        jsonfile["basic analysis"]["rows with many missing values"] = {}

        dataset_missings_columns = dataset.isna().sum()
        for index, value in dataset_missings_columns.items():

            jsonfile["basic analysis"]["missing values in columns"][index] = value

        dataset_missings_rows = dataset.isna().sum(axis=1)
    
        for index, value in dataset_missings_rows[dataset_missings_rows > len(dataset.columns)*0.5].items():

            jsonfile["basic analysis"]["rows with many missing values"][index] = value

        
        return jsonfile

    @staticmethod
    def __detect_outliers(dataset: pd.DataFrame, jsonfile: dict) -> dict:
        """
        Detects outliers in all columns of the dataset containing floats and stores their indices in a JSON file
        ---
        Parameter
        1. dataset to be analyzed
        2. JSON file to write to
        ---
        Return the JSON file with additional data
        """

        jsonfile["basic analysis"]["outlier"] = {}

        dataset_numerics_only = dataset.select_dtypes(include=[np.float])   
    
        for column in dataset_numerics_only:
            
            current_column = dataset_numerics_only[column].dropna()

            current_column_sorted = current_column.sort_values()

            Q1, Q2, Q3 = np.percentile(current_column_sorted, [25,50,75])

            if ((Q3 - Q1) < 0.1) :
                continue
            
            # interquartile range
            IQR = Q3 - Q1

            # calculation of boundaries is still a work in progress
            lower_boundary = Q1 - 2 * IQR
            upper_boundary = Q3 + 2 * IQR

            current_column = (current_column < lower_boundary) | (current_column > upper_boundary)

            outlier_indices = current_column[current_column].index.values.tolist()

            outlier_indices = [index + 1 for index in outlier_indices]

            jsonfile["basic analysis"]["outlier"][column] = outlier_indices
        
        return jsonfile






    

    


    