from flask import Flask

from blog.database import db_session

app = Flask(__name__)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

from blog.controllers import *
