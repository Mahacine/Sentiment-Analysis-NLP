from app import app
from flask import render_template
from app.form import TextForm
from main_nltk import analyze
from main import manual_analyze,convert_counter_to_string
import io
import base64
import matplotlib.pyplot as plt


@app.route('/', methods=['GET', 'POST'])
#@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextForm()
    if form.validate_on_submit():
        if form.upload_file.data:  # Check if a file is uploaded
            file = form.upload_file.data
            file_content = file.stream.read().decode("utf-8")  # Read the content of the file
            text = file_content
        else:
            text = form.text.data
        method = form.method.data
        # Call your method to analyze the text
        if method == 'nltk':
            analysis_result = analyze(text)
        elif method == 'manual':
            emotions_counter = manual_analyze(text)
            analysis_result = convert_counter_to_string(emotions_counter)
        # Populate the answer field with the result
        form.answer.data = analysis_result

        # Generate the plot if 'manual' is chosen
        if method == 'manual':
            fig, x_axis = plt.subplots()
            x_axis.bar(emotions_counter.keys(), emotions_counter.values())
            fig.autofmt_xdate()
            # Save the plot to a buffer
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            # Encode the plot as a base64 string
            plot_data = base64.b64encode(buffer.getvalue()).decode()
            plt.close(fig)
            form.plot.data = plot_data
        # Render the template with the updated form
        return render_template('index.html', title="Sentiment analysis", form=form)
    return render_template('index.html', title="Sentiment analysis", form=form)