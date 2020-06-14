from flask import Blueprint, request, session, url_for, render_template, redirect

from models.user import User


user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email, password)
            session['email'] = email
        except Exception as e:
            return e.message

    return render_template('users/register.html')