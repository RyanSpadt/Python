import json

from flask import Flask, render_template, request

from common.database import Database
from models.item import Item

app = Flask(__name__)


# Initializes database before we do any other request with Flask
@app.before_first_request
def initialize_database():
    Database.initialize()


# Tell endpoint if it receives a POST request to take the data from input fields and process it
@app.route('/', methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']   # Accessing the url field from the form data in the request
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Item(url, tag_name, query).save_to_db()

    return render_template('new_item.html')


if __name__ == '__main__':
    app.run(debug=True)
