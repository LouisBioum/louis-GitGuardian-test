#!/bin/python

import os

from flask import Flask

import time
import locale

locale.setlocale(locale.LC_ALL, '')

from kubernetes import client, config

app = Flask(__name__)

def get_pod_start_time(namespace, app_name):
    """
    find namespace pod
    """
    config.load_incluster_config()
    k8s_api_obj = client.CoreV1Api()
    api_response = k8s_api_obj.list_namespaced_pod(namespace, label_selector="app=" + app_name, limit=56)
    return api_response.items[0].status.start_time.strftime("%I:%M%p")

@app.route('/')
def index():
    return "Hello GitGuardian!"

@app.route('/pod-id')
def pod_id():
    return os.environ['POD_NAME']

@app.route('/startup-time')
def pod_start_time():
    return get_pod_start_time('default', 'sample-app')

app.run(host="0.0.0.0", port=8080)