from flask import Flask, render_template, redirect, url_for, request
from yt2mp4 import download
from os import remove
from time import time
app = Flask(__name__)
app.config['SECRET_KEY'], app.config['SEND_FILE_MAX_AGE_DEFAULT'] = '**************', 0
@app.route('/', methods=['GET', 'POST'])
def index(): return render_template("index.html") if request.method == 'GET' else result(request.form['url'])
def result(url):
    initial_time = time()
    while time() - initial_time <= 300:
        try:
            download(url, outname="static/temp.mp4")
            remove('geckodriver.log')
        except (ValueError, KeyError): continue
        else: break
    else: return "Error: Timeout, check the url and try again."
    return redirect(url_for('static', filename='temp.mp4'))
if __name__ == '__main__': app.run()
