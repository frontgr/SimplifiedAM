from pymongo import MongoClient
from os import getenv


class Database:
    def __init__(self):
        mongo_user = getenv("MONGO_INITDB_ROOT_USERNAME")
        mongo_password = getenv("MONGO_INITDB_ROOT_PASSWORD")
        mongo_location = getenv("APP_DB_LOCATION")
        client = MongoClient(f'mongodb://{mongo_user}:{mongo_password}@{mongo_location}/')
        self.db = client.Test

    def TestDB(self):
        return {'message': 'Just testing!'}
