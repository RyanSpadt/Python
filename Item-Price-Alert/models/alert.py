import uuid
from typing import Dict
from dataclasses import dataclass, field
from models.item import Item
from models.model import Model


@dataclass(eq=False)
class Alert(Model):

    collection: str = field(init=False, default="alerts")
    item_id: str
    price_limit: float
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)

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
