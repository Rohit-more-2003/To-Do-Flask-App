# flask_wtf is a flask module for wt forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired # module to state if value can't be null


# when using wtforms, classes are used for variables
class AddTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Submit')