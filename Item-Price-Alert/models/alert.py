import uuid
from typing import Dict

from common.database import Database
from models.item import Item
from models.model import Model


class Alert(Model):
    
    collection = "alerts"

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        super().__init__(*args, **kwargs)
        self.item_id = item_id
        self.price_limit = price_limit
        self.item = Item.get_by_id(item_id)
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
    def notify_if_price_reached(self) -> None:
        if self.item.price < self.price_limit:
            print(f"item {self.item} has reached a price under {self.price_limit}. Latest price {self.item.price}")
