from flask import Flask, render_template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)

app_name = 'LED Lights'

@app.route('/')
def home():
    page_title = 'LED Lights'
    return render_template('index.html', 
                           app_name = app_name,
                           page_title = page_title)

@app.route('/off')
def off():
    GPIO.output(18, GPIO.LOW)
    return 'light off'

@app.route('/on')
def on():
    GPIO.output(18, GPIO.HIGH)
    return 'light on'

if __name__ == '__main__':
    app.run(host='192.168.0.63', port=80, debug=True, threaded=False)