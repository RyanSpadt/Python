import uuid
from typing import Dict, List

from common.database import Database
from models.item import Item


class Alert:

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        self.item_id = item_id
        self.price_limit = price_limit
        self.item = Item.get_by_id(item_id)
        self.collection = "alerts"
        self._id = _id or uuid.uuid4().hex

    # Returns data in json format as a Dict, this is the information we want stored in our DB
    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "item_id": self.item_id
        }

    # Loads the price of the item
    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    # Notifies the user in this case, us, when the price of the item has gone under the desired price.
    # In the future this will email the user
    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"item {self.item} has reached a price under {self.price_limit}. Latest price {self.item.price}")

    # Inserts our data into the collection defined in __init__ method in the format of the json() method
    def save_to_db(self) -> None:
        Database.insert(self.collection, self.json())

    # Will return a set of alert objects
    @classmethod
    def all(cls) -> List:
        alerts_from_db = Database.find("alerts", {})
        return[cls(**alert) for alert in alerts_from_db]