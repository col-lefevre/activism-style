from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html', page_css=url_for('static', filename='css/index.html'))