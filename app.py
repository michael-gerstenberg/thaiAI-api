#!/usr/bin/env python3.6
import os
import json
from flask import Flask
from flask import render_template, request
from tltk import nlp

app = Flask(__name__)



####
# Info
# supervisorctl restart flask

@app.route("/")
def index():
  message = "Hello thomas from project_name"
  return render_template('index.html', message=message)

@app.route("/syl_segment", methods = ['GET', 'POST'])
def syl_segment():
  if request.method == 'GET':
    return 'Please use Post'
  elif request.method == 'POST':
    data = request.get_json(force=True)
    result = nlp.syl_segment(data['text'])
    return json.dumps({"result":result})
if __name__== "__main__":
  app.run(host='0.0.0.0', port=1024, debug=True)
