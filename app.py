from flask import Flask



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key' # necessary to use csrf_token of the form


from routes import *


if __name__ == "__main__":
    app.run(debug=True)