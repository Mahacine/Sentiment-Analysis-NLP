from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TextForm(FlaskForm):
    text = StringField('How are you feeling today ?', validators=[DataRequired()])
    submit = SubmitField('Analyze')