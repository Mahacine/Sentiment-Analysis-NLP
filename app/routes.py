from app import app
from flask import render_template
from app.form import TextForm

@app.route('/')
@app.route('/index')
def index():
    form = TextForm()
    if form.validate_on_submit():
        text = form.text.data
        return "Success"
    return render_template('index.html', title="Sentiment analysis", form=form)