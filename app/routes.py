from app import app
from flask import render_template
from app.form import TextForm
from main_nltk import analyze

@app.route('/', methods=['GET', 'POST'])
#@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():
        text = form.text.data
        # Call your method to analyze the text
        analysis_result = analyze(text)
        # Populate the answer field with the result
        form.answer.data = analysis_result
        # Render the template with the updated form
        return render_template('index.html', title="Sentiment analysis", form=form)
    return render_template('index.html', title="Sentiment analysis", form=form)