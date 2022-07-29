
from xmlrpc.client import boolean
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.objectid import ObjectId
from mongomock import MongoClient as MongoMockClient

class Database:
    """
    MongoDB database interface API.
    ---
    Do not use independently, always use the public DataStorage API.
    ---
    Everything regarding MongoDB should live in this class.
    """

    def __init__(self, server_url="mongodb://root:example@localhost"):
        if server_url is not None:
            self.__mongo = Database.__use_real_database(server_url)
        else:
            self.__mongo = MongoMockClient()


    def __use_real_database(server_url: str) -> MongoClient:
        """
        Connects to a MongoDB database at the url.
        ---
        Parameter
        1. server url with host as defined in docker-compose.yml
        ---
        Returns database interface
        """
        try:
            # sample credentials from docker-compose
            # NOTE: when running this script in a container defined in docker-compose.yml,
            #       the url for MongoClient needs to match the database service name
            #       --> eg. "mongodb://root:example@mongo"
            mongo = MongoClient(server_url, 27017,
                # timeout to find a database server
                serverSelectionTimeoutMS=30000)
            
            # we want to fail as fast as possible when the database is not reachable.
            #   by default pymongo will lazy initialize and waits for the first 'real' database 
            #   interaction to connect to MongoDB
            mongo.list_databases()

            return mongo
        except:
            raise Exception("cannot find MongoDB! URL "+ server_url +"\n    Did you forget to launch it with `docker-compose up --build mongo`?")
        
    def CheckIfUserExists(self, username: str) -> bool:
        """
        Check if user exists by checking if his database exists
        ---
        Parameter
        1. username: name of the user
        ---
        Returns database existance status, TRUE == EXITS
        """
        if username in self.__mongo.list_databases() == True:
            return True
        else:
            return False

    def InsertDataset(self, username: str, dataset: 'dict[str, str]') -> str:
        """
        Insert dataset
        ---
        Parameter
        1. username
        2. dataset as dict
        ---
        Returns dataset id
        """
        datasets: Collection = self.__mongo[username]["datasets"]
        result = datasets.insert_one(dataset)
        return str(result.inserted_id)

    def GetDatasets(self, username: str) -> 'list[dict[str, object]]':
        """
        Get a dataset byy it"s name
        ---
        Parameter
        1. username
        2. dataset name
        ---
        Returns dataset as dict
        """
        datasets: Collection = self.__mongo[username]["datasets"]
        return datasets.find()

    def GetDataset(self, username: str, filter: 'dict[str, object]') -> 'dict[str, object]':
        """
        Get a dataset by it's name
        ---
        Parameter
        1. username
        2. dataset name
        ---
        Returns dataset as dict or `None`
        """
        datasets: Collection = self.__mongo[username]["datasets"]
        return datasets.find_one(filter)

    def UpdateDataset(self, username: str, id: str, new_values: 'dict[str, object]') -> bool:
        """
        Update a dataset record
        ---
        Parameter
        1. username
        2. dataset id
        3. dictionary of new values
        ---
        Returns `True` if a record was updated otherwise `False`
        """
        datasets: Collection = self.__mongo[username]["datasets"]
        result = datasets.update_one({ "_id": ObjectId(id) }, { "$set": new_values })
        return result.modified_count >= 1


    def InsertTraining(self, username: str, training_config: 'dict[str, str]'):
        """
        Insert training
        ---
        Parameter
        1. username
        2. training as dict
        ---
        Returns training id
        """
        trainings: Collection = self.__mongo[username]["trainings"]
        result = trainings.insert_one(training_config)
        return str(result.inserted_id)

    def GetTraining(self, username: str, id: str) -> 'dict[str, object]':
        """
        Get a training by it's id
        ---
        Parameter
        1. username
        2. training id
        ---
        Returns training as dict
        """
        trainings: Collection = self.__mongo[username]["trainings"]
        return trainings.find_one({ "_id": ObjectId(id) })

    def GetTrainings(self, username: str) -> 'list[dict[str, object]]':
        """
        Get all trainings from a user
        ---
        Parameter
        1. username
        ---
        Returns trainings as list of dicts
        """
        trainings: Collection = self.__mongo[username]["trainings"]
        return trainings.find()

    def UpdateTraining(self, username: str, id: str, new_values: 'dict[str, str]') -> bool:
        """
        Update a training record
        ---
        Parameter
        1. username
        2. training id
        3. dictionary of new values
        ---
        Returns `True` if a record was updated otherwise `False`
        """
        trainings: Collection = self.__mongo[username]["trainings"]
        result = trainings.update_one({ "_id": ObjectId(id) }, { "$set": new_values })
        return result.modified_count >= 1


    def InsertModel(self, username: str, model_details: 'dict[str, str]') -> str:
        """
        Insert model
        ---
        Parameter
        1. username
        2. model as dict
        ---
        Returns model id
        """
        models: Collection = self.__mongo[username]["models"]
        result = models.insert_one(model_details)
        return str(result.inserted_id)

    def UpdateModel(self, username: str, id: str, new_values: 'dict[str, str]') -> bool:
        """
        Update a model record
        ---
        Parameter
        1. username
        2. training id
        3. dictionary of new values
        ---
        Returns `True` if a record was updated otherwise `False`
        """
        models: Collection = self.__mongo[username]["models"]
        result = models.update_one({ "_id": ObjectId(id) }, { "$set": new_values })
        return result.modified_count >= 1

    def GetModels(self, username: str, filter: str=None) -> 'list[dict[str, object]]':
        """
        Get all models from a user
        ---
        Parameter
        1. username
        2. optional filter
        ---
        Returns models as list of dicts
        """
        models: Collection = self.__mongo[username]["models"]
        return models.find(filter)

    def GetModel(self, username: str, id: str) -> 'dict[str, object]':
        """
        Get a model by it's id
        ---
        Parameter
        1. username
        2. model id
        ---
        Returns training as dict
        """
        models: Collection = self.__mongo[username]["models"]
        return models.find_one({ "_id": ObjectId(id) })


    def DropDatabase(self, username: str):
        """
        Delete all datasets sessions and models for a user
        ---
        Parameter
        1. username
        """
        self.__mongo.drop_database(username)
