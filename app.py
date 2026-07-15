from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', current_title="Custom Title")


@app.route('/add')
def add_task():
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)