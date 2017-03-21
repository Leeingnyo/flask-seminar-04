from flask import Flask
app = Flask(__name__)

from blog.controllers import *
