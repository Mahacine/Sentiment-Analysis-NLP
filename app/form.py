from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired
#from flask_wtf.file import FileRequired

class TextForm(FlaskForm):

    upload_file = FileField('Upload a file')
    text = TextAreaField('--Or-- Enter your text', render_kw={"rows": 5})
    submit = SubmitField('Analyze')
    answer = TextAreaField('Analysis Result', render_kw={"rows": 5, "readonly": True})
    method = SelectField('Choose analysis method', choices=[('nltk', 'NLTK'), ('manual', 'Manual')], validators=[DataRequired()])
    plot = TextAreaField('Plot', render_kw={"style": "display:none;"})  # Hidden field for the plot data

    def validate(self, extra_validators=None):
        if not super(TextForm, self).validate(extra_validators=extra_validators):
            return False

        if not self.upload_file.data and not self.text.data:
            error_msg = "Please upload a file or enter text."
            self.upload_file.errors.append(error_msg)
            self.text.errors.append(error_msg)
            return False

        return True