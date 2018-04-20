#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
from flask import Flask, render_template, url_for, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/data/<file_name>')
def data(file_name):
    path = './outputs/'+file_name+'.json'
    print('file '+path+' was requested')
    if os.path.isfile(path):
        f = file(path, 'r')
        return f.read()
    else:
        err = jsonify({'error':file_name+' not found'})
        return err, 404    

