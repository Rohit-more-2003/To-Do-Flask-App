from flask import render_template, redirect, url_for, flash, get_flashed_messages
from datetime import datetime, UTC

from app import app, db
import forms
from models import Task

@app.route('/')
@app.route('/index')
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

        flash("Task added to database successfully!")

        return redirect(url_for('index'))

    return render_template('add.html', form=form)


@app.route('/edit/<int:task_id>', methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get(task_id)
    # print(task)

    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.now(UTC).date()
            
            db.session.commit()

            flash('Task has been updated successfully!')
            return redirect(url_for('index'))

        form.title.data = task.title

        return render_template('edit.html', task_id=task_id, form=form)

    else:
        flash("Task Not Found!")    

    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=["GET", "POST"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    # print(task)

    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()

            flash('Task has been deleted successfully!')
            return redirect(url_for('index'))

        return render_template('delete.html', task_id=task_id, form=form, title=task.title)
    
    else:
        flash("Task Not Found!")

    return redirect(url_for('index'))