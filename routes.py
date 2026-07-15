from flask import render_template

from app import app
import forms

@app.route('/index')
def index():
    return render_template('index.html', current_title="Custom Title")


@app.route('/add', methods=['GET', 'POST']) # Deafault is methods=['POST']
def add_task():
    form = forms.AddTaskForm()

    if form.validate_on_submit():
        print('Submitted title', form.title.data)

        return render_template('add.html', form=form, title=form.title.data)

    return render_template('add.html', form=form)