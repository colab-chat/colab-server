from flask import Blueprint, render_template
from flask_user import login_required


# -------------------------------
# Main blueprint
# -------------------------------
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@login_required
def index():
    print("INDEX PAGE")
    return render_template('index.html')
