from flask import Flask

app = Flask(__name__)

from webserver import errors
from webserver import filters
from webserver import routes