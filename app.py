from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def index():
    # index_path = os.get_
    return render_template('index.html', current_title="Custom Title")

if __name__ == "__main__":
    app.run(debug=True)