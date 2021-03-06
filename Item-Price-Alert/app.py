from flask import Flask

from common.database import Database

from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint


app = Flask(__name__)

app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(user_blueprint, url_prefix='/users')


# Initializes database before we do any other request with Flask
@app.before_first_request
def initialize_database():
    Database.initialize()


if __name__ == '__main__':
    app.run(debug=True)
