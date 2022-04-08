import json
import os.path
from JsonUtil import get_config_property

from TabularDataAutoML import TabularDataAutoML

if __name__ == '__main__':
    file_path = os.path.join(get_config_property("job-file-path"),
                             get_config_property("job-file-name"))
    with open(file_path) as file:
        process_json = json.load(file)

    tabular_data_automl = TabularDataAutoML(process_json)

    if process_json["task"] == 1:
        # Classification
        tabular_data_automl.classification()