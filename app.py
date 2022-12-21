from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'prohealth'

@app.route("/")
def index():
    session["x"] = "test"
    return render_template('index.html', page_css=url_for('static', filename='css/index.css'), page_title='Home')

@app.route("/test")
def test():
    print(session["x"])
    return render_template('index.html', page_css=url_for('static', filename='css/index.css'), page_title='Home')