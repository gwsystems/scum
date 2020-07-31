# Button press raises pin 15 high to trigger mosfet
# stays on until button is released

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP) # button
GPIO.setup(15,GPIO.OUT) # mosfet

pressed = False
count = 0

# start with mosfet off
GPIO.output(15,GPIO.LOW)

# Infinite loop
while True:
    # If button is pressed
    if (GPIO.input(10) == GPIO.LOW and pressed == False):
        print("pressed, triggering mosfet")

        GPIO.output(15,GPIO.HIGH)
        time.sleep(0.05) # 0.25 delay in seconds
        
    # If button is not pressed
    if (GPIO.input(10) == GPIO.HIGH):
        pressed = False
        GPIO.output(15,GPIO.LOW)
