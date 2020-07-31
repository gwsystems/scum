# run with `sudo python servo.py`
# servo doesn't turn all the way. SetAngle is wrong

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(3, 50)
p.start(2.5)

try:
    while True:
        p.ChangeDutyCycle(2.5) # turn towards 0 degree
        time.sleep(1) # sleep 1 second
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1) # sleep 1 second
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()




# Don't use this function, the angle might not be accurate
def SetAngle(angle):
    duty = angle /20
    GPIO.output(3,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3,False)
    pwm.ChangeDutyCycle(0)


