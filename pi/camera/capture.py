# simple script for img capture
# takes 1 arg: filename (.jpg)
import sys
from picamera import PiCamera
from time import sleep

# create instance
camera = PiCamera()
 
# Takes a string, ie. 'img.jpg'
def capture(filename):
   
    # camera needs time to adjust brightness
    # this is the shortest delay
    sleep(0.15)
    
    # capture and save img as filename
    camera.capture(filename)

filename = 'img.jpg'
if len(sys.argv) == 2:
    filename = sys.argv[1]
capture(filename)
print('captured ' + filename)

