from flask import Flask, render_template
import RPi.GPIO as GPIO


# GPIO.cleanup()
# testing some other junk

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

app = Flask(__name__)
app.debug = True

app_name = 'LED Lights'

@app.route('/')
def home():
    page_title = 'LED Lights'
    return render_template('index.html', 
                           app_name = app_name,
                           page_title = page_title)


@app.route('/<light>/<status>', methods=['POST'])
def light_status(light, status):
    if light == "white":
        light = 18
    elif light == "red":
        light = 17
    if status == "on":
        status = GPIO.HIGH
    elif status == "off":
        status = GPIO.LOW
    GPIO.output(light, status)  
    # if light == 'white':
    #     if status == 'on':
    #         GPIO.output(18, GPIO.HIGH)
    #         return 'white light on'
    #     elif status == 'off':
    #         GPIO.output(18, GPIO.LOW)
    #         return 'white light off'
    # elif light == 'red':
    #     if status == 'on':
    #         GPIO.output(17, GPIO.HIGH)
    #         return 'red light on'
    #     elif status == 'off':
    #         GPIO.output(17, GPIO.LOW)
    #         return 'red light off'
    # else:
    #     return 'Invalid light'
    return 'ok'

if __name__ == '__main__':
    app.run(host='192.168.0.63', port=80, debug=True, threaded=False)