from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', page_css=url_for('static', filename='css/index.css'), page_title='Home')