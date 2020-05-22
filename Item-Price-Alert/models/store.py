import uuid
import re
from typing import Dict
from dataclasses import dataclass, field
from models.model import Model


@dataclass(eq=False)
class Store(Model):

    collection: str = field(init=False, default="stores")
    name: str
    url_prefix: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    # Our json method for what we want saved to MongoDB
    def json(self) -> Dict:
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    # Method will go into our database and search for a singular object by name
    @classmethod
    def get_by_name(cls, store_name: str) -> "Store":
        return cls.find_one_by("name", store_name)

    # Searches database for a url string that starts with url_prefix but could be longer
    @classmethod
    def get_by_url_prefix(cls, url_prefix: str) -> "Store":
        url_regex = {"$regex": "^{}".format(url_prefix)}
        return cls.find_one_by("url_prefix", url_regex)

    # Returns a store from a url within our database up to the forward slash ex(https://johnlewis.com/)
    # Anything after that final forward slash will be ignored.
    @classmethod
    def find_by_url(cls, url: str) -> "Store":
        pattern = re.compile(r"https?://.*?/")
        match = pattern.search(url)
        url_prefix = match.group(1)
        return cls.get_by_url_prefix(url_prefix)
