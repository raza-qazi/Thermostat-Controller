from app import app
from flask import Flask, redirect, url_for, request, render_template, jsonify
import datetime


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user = request.form['formbox']
        return render_template('index.html',
                               title='Thermostat', user="Sir", form=user)
    elif request.method == 'GET':
        return render_template('index.html',
                               title='Thermostat', user="Sir")


@app.route('/time')
def time():
    temp = datetime.datetime.time(datetime.datetime.now())
    return render_template('time.html', title="Current Time", temp=str(temp))


@app.route('/_status', methods=['GET',  'POST'])
def update_time():
    temp = datetime.datetime.time(datetime.datetime.now())
    return jsonify(title="Current Time", temp=str(temp))
