from typing import Dict
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
import requests
import re
import uuid

from models.model import Model


@dataclass(eq=False)
class Item(Model):

    collection: str = field(init=False, default="items")
    url: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    # Properties of the object that we want stored.
    def __post_init__(self):
        self.price = None
    
    # Returns a Dict of our objects properties to store in our DB
    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query
        }

    # Accesses object properties to obtain the price of the item we want from the website.
    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        # if there's a comma you can put ,? as an optional. \d+ means we expect at least 1 number or more. \d* means 0 or more
        pattern = re.compile(r"(\d*,?\d+\.\d\d)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")
        self.price = float(without_commas)
        
        return self.price
