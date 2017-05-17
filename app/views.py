from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template('index.html',
                           app_name="CoLab",
                           message='this is a message')
