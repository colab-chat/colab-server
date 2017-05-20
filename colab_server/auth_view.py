from flask import Blueprint, render_template, redirect
from .auth_forms import LoginForm


# -------------------------------
# Main blueprint
# -------------------------------
auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login', methods=['GET'])
def login_get():
    print("GETTING")
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    return render_template('login.html',
                           form=form)


@auth.route('/login', methods=['POST'])
def login_post():
    form = LoginForm()
    if form.validate_on_submit():
        print("YAYA")
        return "Logged in"
    return "Not logged in"
