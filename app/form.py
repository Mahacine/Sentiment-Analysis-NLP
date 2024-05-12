from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    text = TextAreaField('How are you feeling today?', validators=[DataRequired()], render_kw={"rows": 5})
    submit = SubmitField('Analyze')
    answer = TextAreaField('Analysis Result', render_kw={"rows": 5, "readonly": True})
    method = SelectField('Choose analysis method', choices=[('nltk', 'NLTK'), ('manual', 'Manual')], validators=[DataRequired()])
    plot = TextAreaField('Plot', render_kw={"style": "display:none;"})  # Hidden field for the plot data