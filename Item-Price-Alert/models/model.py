from abc import ABCMeta, abstractmethod
from typing import List

from common.database import Database


# metaclass gives this class the ability to use abstract methods.
class Model(metaclass=ABCMeta):
    
    collection = "models"

    def __init__(self, *args, **kwargs):
        pass

    # If we have a model it must have a json method. It is the definition of what our models should contain.
    @abstractmethod
    def json(self):
        raise NotImplementedError
        
    # Upserts the database based on unique id "_id", it either inserts a new one
    # Or if it exists already updates the existing.
    def save_to_db(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    # Removes data from collection based on "_id"
    def remove_from_db(self):
        Database.remove(self.collection, {"_id": self._id})

    # Will return a set of alert objects
    # For item models call Item.all(); for alert models call Alert.all()
    # Errors will exist inside this class because collection is not defined here but in sub classes.
    @classmethod
    def all(cls) -> List:
        elements_from_db = Database.find(cls.collection, {})
        return[cls(**elem) for elem in elements_from_db]
    
    # Searches database in a collection for an _id and returns that singular object
    @classmethod
    def get_by_id(cls, _id: str):
        return cls.find_one_by("_id", _id)

    # Returns a singular item by searching a collection by url
    @classmethod
    def find_one_by(cls, attribute, value): # Item.find_one_by('url', 'https://blank.com
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    # Returns a list of items by search a collection by url
    @classmethod
    def find_many_by(cls, attribute, value):
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
