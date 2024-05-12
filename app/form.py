from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    text = TextAreaField('How are you feeling today?', validators=[DataRequired()], render_kw={"rows": 5})
    submit = SubmitField('Analyze')
    answer = TextAreaField('Analysis Result', render_kw={"rows": 5, "readonly": True})