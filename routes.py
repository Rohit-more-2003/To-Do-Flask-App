from flask import render_template, redirect, url_for
from datetime import datetime, UTC

from app import app, db
import forms
from models import Task

@app.route('/')
def index():
    tasks = Task.query.all()

    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST']) # Default is methods=['POST']
def add_task():
    form = forms.AddTaskForm()

    if form.validate_on_submit():
        # print('Submitted title', form.title.data)
        task = Task(title=form.title.data, date=datetime.now(UTC).date())
        db.session.add(task)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html', form=form)