from flask import Flask

from common.database import Database
from views.items import item_blueprint


app = Flask(__name__)

app.register_blueprint(item_blueprint, url_prefix="/items")


# Initializes database before we do any other request with Flask
@app.before_first_request
def initialize_database():
    Database.initialize()


if __name__ == '__main__':
    app.run(debug=True)
