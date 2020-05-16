import json

from flask import request, render_template, Blueprint

from models.item import Item

item_blueprint = Blueprint('items', __name__)


# An index of the items page, gives a list of all items currently stored in our application.
@item_blueprint.route('/')
def index():
    items = Item.all()
    return render_template('items/index.html', items=items)


# Tell endpoint if it receives a POST request to take the data from input fields and process it
@item_blueprint.route('/new', methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        url = request.form['url']   # Accessing the url field from the form data in the request
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Item(url, tag_name, query).save_to_db()

    return render_template('items/new_item.html')
