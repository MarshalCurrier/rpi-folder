
from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home'

@app.route('/off')
def off():
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()
    return 'light off'

@app.route('/on')
def on():
    GPIO.output(18, GPIO.HIGH)
    return 'light on'

if __name__ == '__main__':
    app.run(host='192.168.0.63', port=80, debug=True, threaded=False)