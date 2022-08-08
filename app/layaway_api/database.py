from asyncore import read
from pymongo import MongoClient
from bson.json_util import dumps


class Database:
    def __init__(self):
        self.client = MongoClient('mongodb://root:root@mongo_container:27017')

        database = 'marvel-comics'
        collection = 'users_layaway'
        cursor = self.client[database]
        self.collection = cursor[collection]

    def read(self, credentials):
        return self.collection.find_one(credentials)

    def write(self, new_document):
        self.collection.insert_one(new_document)

    def update(self, reference, document):
        self.collection.update_many(reference, document)
