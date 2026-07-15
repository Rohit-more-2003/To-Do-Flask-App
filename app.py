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



if __name__ == "__main__":
    app.run(debug=True)