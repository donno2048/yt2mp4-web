from flask import Flask, render_template, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from yt2mp4 import download
from os import remove
from time import time
class DownloadForm(FlaskForm): url, submit = StringField('url', render_kw={'placeholder': 'https://www.youtube.com/watch?v=***********'}, validators=[DataRequired()]), SubmitField('submit')
app = Flask(__name__)
app.config['SECRET_KEY'], app.config['SEND_FILE_MAX_AGE_DEFAULT'] = '**************', 0
@app.route('/', methods=['GET', 'POST'])
def index():
    form = DownloadForm()
    return result(form.url) if form.validate_on_submit() and form.url.data != "" else render_template("index.html", form=form)
def result(url):
    initial_time = time()
    while time() - initial_time <= 300:
        try:
            download(url.data, outname="static/temp.mp4")
            remove('geckodriver.log')
        except (ValueError, KeyError): continue
        else: break
    else: return "Error: Timeout, check the url and try again."
    return redirect(url_for('static', filename='temp.mp4'))
if __name__ == '__main__': app.run()
