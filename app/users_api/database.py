from pymongo import MongoClient
from bson.json_util import dumps


class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://root:root@mongo_container:27017')

        database = 'marvel-comics'
        collection = 'users'
        cursor = self.client[database]
        self.collection = cursor[collection]

    def read(self, credentials):
        return self.collection.find_one(credentials)

    def write(self, new_document):
        response = self.collection.insert_one(new_document)
        new_document['id'] = str(response.inserted_id)
        return dumps(new_document)
