from flask import render_template

from app import app
import forms

@app.route('/index')
def index():
    return render_template('index.html', current_title="Custom Title")


@app.route('/add')
def add_task():
    form = forms.AddTaskForm()
    return render_template('add.html', form=form)