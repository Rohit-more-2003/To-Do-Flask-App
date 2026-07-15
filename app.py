from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key' # necessary to use csrf_token of the form
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


db = SQLAlchemy(app=app) # initiated db instance
# bash commands to create the db
# python3 - creates a python bash in terminal
# from app import db
# db.create_all()


from routes import *


def create_database():
    """
    Creates a database if it does not exists and connects with flask app,
    else just connects with flask app.
    """

    # app.app_context determines the action is done when the app runs
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    create_database()
    app.run(debug=True)