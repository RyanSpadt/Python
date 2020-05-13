from models.item import Item


url = "https://www.johnlewis.com/2020-apple-ipad-pro-11-inch-a12z-bionic-ios-wi-fi-128gb/p4949052"
tag_name = "p"
query = {"class": "price price--large"}

ipad = Item(url, tag_name, query)

print(ipad.load_price())
