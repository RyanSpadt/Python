from flask import Blueprint, render_template, request, url_for, redirect

from models.alert import Alert
from models.item import Item
from models.store import Store

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    alerts = Alert.all()
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def new_alert():
    if request.method == 'POST':
        alert_name = request.form['name']
        item_url = request.form['item_url']
        price_limit = float(request.form['price_limit'])

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        item.save_to_db()

        Alert(alert_name, item._id, price_limit).save_to_db()

    return render_template('alerts/new_alert.html')


@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST'])
def edit_alert(alert_id):
    alert = Alert.get_by_id(alert_id)

    if request.method == 'POST':
        price_limit = float(request.form['price_limit'])

        alert.price_limit = price_limit
        alert.save_to_db()

        return redirect(url_for('.index'))

    return render_template('alerts/edit_alert.html', alert=alert)


@alert_blueprint.route('/delete/<string:alert_id>')
def delete_alert(alert_id):
    Alert.get_by_id(alert_id).remove_from_db()
    return redirect(url_for('.index'))

