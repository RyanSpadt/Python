from models.item import Item
from common.database import Database
from models.alert import Alert


ipad = Item("https://www.johnlewis.com/2020-apple-ipad-pro-11-inch-a12z-bionic-ios-wi-fi-128gb/p4949052",
            "p",
            {"class": "price price--large"})

Database.initialize()

ipad.save_to_db()

items_loaded = Item.all()
print(items_loaded)
print(items_loaded[0].load_price())

alert = Alert("2400bf3988bb44e187bf0e44524838dc", 2000)
alert.save_to_db()

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")
