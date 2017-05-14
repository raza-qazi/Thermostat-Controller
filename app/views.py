import datetime

from flask import request, render_template, jsonify

from app import app

temperature = 1


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    global temperature
    if request.method == 'POST':
        box = request.form['formbox']
        return render_template('index.html',
                               title='Thermostat', form=box, temp=temperature)
    elif request.method == 'GET':
        return render_template('index.html',
                               title='Thermostat', temp=temperature)


@app.route('/time')
def time():
    time = datetime.datetime.time(datetime.datetime.now())
    test()
    return render_template('time.html', title="Current Time", temp=str(time))


@app.route('/_status', methods=['GET', 'POST'])
def update_time():
    time = datetime.datetime.time(datetime.datetime.now())
    return jsonify(title="Current Time", temp=str(time))


@app.route('/button')
def button():
    global temperature
    return render_template('button.html', title="Button Demo", temp=temperature)


@app.route('/_incTemp', methods=['GET', 'POST'])
def inc_button():
    global temperature
    temperature += 1
    return str(temperature)


@app.route('/_currentTemp', methods=['GET', 'POST'])
def update_temp():
    global temperature
    return str(temperature)
