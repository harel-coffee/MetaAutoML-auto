from AutoMLManager import AutoMLManager


class AutoKerasManager(AutoMLManager):
    name = "Auto_Keras"

    def __init__(self, configuration, folder_location, session_id):
        automl_service_host = 'AUTOKERAS_SERVICE_HOST'
        automl_service_port = 'AUTOKERAS_SERVICE_PORT'
        super(AutoKerasManager, self).__init__(configuration, folder_location, automl_service_host, automl_service_port,
                                               session_id)