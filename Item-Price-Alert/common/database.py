from typing import Dict

import pymongo


class Database:
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['pricing']

    # inserts our data into our collection in our mongo DB
    @staticmethod
    def insert(collection: str, data: Dict) -> None:
        Database.DATABASE[collection].insert(data)

    # Searches Database by query in a desired collection and returns them
    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)
    
