from flask import Flask
from flask import render_template
from flask import request
import serial

ser = serial.Serial('COM3', 9600)
pos = open('last_pos.txt', 'w')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    text = request.form['fname']
    n = int(text)
    print(n)
    n = 180 - (1.8 * int(n))
    n = int(n)
    n = str(n)
    vol = bytes(n + '\n', 'utf-8')
    ser.write(vol)
    return render_template('index.html')

def volume(n):
    n = 180 - (1.8 * int(n))
    n = int(n)
    n = str(n)
    vol = bytes(n + '\n', 'utf-8')
    ser.write(vol)

app.run()
