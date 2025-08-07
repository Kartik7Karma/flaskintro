from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    content = StringField('Task', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Submit')
