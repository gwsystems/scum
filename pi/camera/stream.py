import cv2
import numpy as np 
from picamera.array import PiRGBArray
from picamera import PiCamera 

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10

rawCapture = PiRGBArray(camera, size=(640, 480))

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	image = frame.array
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	cv2.imshow("frame", image)

	key = cv2.waitKey(1)
	rawCapture.truncate(0)
	if key == 27:
		break

cv2.destroyAllWindows()
