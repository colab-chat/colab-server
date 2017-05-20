from flask import Blueprint, render_template, redirect

from colab_server.auth.forms import (CoLabLoginForm, CoLabRegisterForm)

# -------------------------------
# Main blueprint
# -------------------------------
auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET'])
def login():
    print("GETTING")
    form = CoLabLoginForm()
    if form.validate_on_submit():
        return redirect('flask_user/login.html')
    return render_template('flask_user/login.html',
                           form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    form = CoLabLoginForm()
    if form.validate_on_submit():
        print("YAYA")
        return "Logged in"
    return "Not logged in"


@auth.route('/register', methods=['GET'])
def register():
    form = CoLabRegisterForm()
    return render_template('flask_user/register.html',
                           form=form)


@auth.route('/register', methods=['POST'])
def register_post():
    form = CoLabRegisterForm()
    if form.validate_on_submit():
        return "registered"
    return "not registered"
