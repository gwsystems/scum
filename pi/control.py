# This opens and closes a flap via a button press
# Run with `sudo python servo_and_button.py`

# GPIO pin 3 for the servo
# GPIO pin 10 for the button

# Adapted from: https://projectiot123.com/2019/02/01/raspberry-pi-gpio-programming-example-for-servo-motor-using-python/

import RPi.GPIO as GPIO
import time
from rpi_ws281x import *
import argparse


# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def fill(strip, color, wait_ms=0):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP) #initial state is low
GPIO.setup(3, GPIO.OUT) # servo
GPIO.setup(13,GPIO.OUT) # mosfet


pressed = False
count = 0

# start with mosfet off
GPIO.output(13,GPIO.LOW)


p = GPIO.PWM(3, 50)

# 180 degree is up
# 0 degree is down
p.start(12.5) # start at up position

    # Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
strip.begin()


try:
    while True:
        
        fill(strip, Color(0, 0, 0))  # nothing
        # Button pressed 
        if (GPIO.input(10) == GPIO.LOW and pressed == False):
            print("pressed, triggering mosfet")

            fill(strip, Color(0, 255, 0))  # green
            #time.sleep(2)


            GPIO.output(13,GPIO.HIGH)
            print("pressed")
            p.ChangeDutyCycle(2.5) # turn towards 0 degree
            time.sleep(1) # sleep 1 second
            p.ChangeDutyCycle(12.5) # turn towards 180 degree
            time.sleep(1) # sleep 1 second
            GPIO.output(13,GPIO.LOW)
        
        # Button not pressed
        if (GPIO.input(10) == GPIO.HIGH):
            pressed = False
            GPIO.output(13,GPIO.LOW)
#            fill(strip, Color(0, 0, 0))  # nothing

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
