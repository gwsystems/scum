# This opens and closes a flap via a button press
# Run with `sudo python servo_and_button.py`

# GPIO pin 3 for the servo
# GPIO pin 10 for the button

# Adapted from: https://projectiot123.com/2019/02/01/raspberry-pi-gpio-programming-example-for-servo-motor-using-python/

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP) #initial state is low
GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(3, 50)

# 180 degree is up
# 0 degree is down
p.start(12.5) # start at up position

try:
    while True:
        # Button pressed 
        if (GPIO.input(10) == GPIO.LOW and pressed == False):
            print("pressed")
            p.ChangeDutyCycle(2.5) # turn towards 0 degree
            time.sleep(1) # sleep 1 second
            p.ChangeDutyCycle(12.5) # turn towards 180 degree
            time.sleep(1) # sleep 1 second
        
        # Button not pressed
        if (GPIO.input(10) == GPIO.HIGH):
            pressed = False

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
