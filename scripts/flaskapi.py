#!/bin/python
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello GitGuardian!"

@app.route('/pod-id')
def podid():
    return os.environ['POD_NAME']

app.run(host="0.0.0.0", port=8080)