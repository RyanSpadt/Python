from abc import ABCMeta, abstractmethod
from typing import List

from common.database import Database


# metaclass gives this class the ability to use abstract methods.
class Model(metaclass=ABCMeta):

    # If we have a model it must have a json method. It is the definition of what our models should contain.
    @abstractmethod
    def json(self):
        raise NotImplementedError

    # Will return a set of alert objects
    # For item models call Item.all(); for alert models call Alert.all()
    # Errors will exist inside this class because collection is not defined here but in sub classes.
    @classmethod
    def all(cls) -> List:
        elements_from_db = Database.find(cls.collection, {})
        return[cls(**elem) for elem in elements_from_db]
