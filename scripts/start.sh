#!/bin/bash
pip install kubernetes
pip install -r requirements.txt
python3 /scripts/flaskapi.py
