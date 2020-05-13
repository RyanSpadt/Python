from models.item import Item
from common.database import Database


ipad = Item("https://www.johnlewis.com/2020-apple-ipad-pro-11-inch-a12z-bionic-ios-wi-fi-128gb/p4949052",
            "p",
            {"class": "price price--large"})

Database.initialize()

ipad.save_to_db()

items_loaded = Item.all()
print(items_loaded)
print(items_loaded[0].load_price())
