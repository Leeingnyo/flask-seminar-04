from flask import render_template, request, redirect, url_for
from blog import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
