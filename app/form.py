from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired

class TextForm(FlaskForm):
    upload_file = FileField('Upload a file')
    text = TextAreaField('--Or-- Enter your text', render_kw={"rows": 5})
    submit = SubmitField('Analyze')
    answer = TextAreaField('Analysis Result', render_kw={"rows": 5, "readonly": True})
    method = SelectField('Choose analysis method', choices=[('nltk', 'NLTK'), ('manual', 'Manual')], validators=[DataRequired()])
    plot = TextAreaField('Plot', render_kw={"style": "display:none;"})  # Hidden field for the plot data