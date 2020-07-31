# Identifies objects on a static background, uses HSV colorspace instead of RGB

# Adapted from:
# https://maker.pro/raspberry-pi/tutorial/how-to-create-object-detection-with-opencv


import cv2
import numpy as np 
from picamera.array import PiRGBArray
from picamera import PiCamera 
from time import sleep

# Empty function for trackerbar
def nothing(x):
    pass

# Setup slider window
cv2.namedWindow("Adjust")
cv2.createTrackbar("Threshold", "Adjust", 0, 60, nothing)

# Initialize camera object
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(640, 480)) # 3d array (rows,columns,colors)




# use_video_port true to treat stream as video
count = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    # Use first few frames to get background 
    if count < 10:
        background = cv2.cvtColor(frame.array, cv2.COLOR_BGR2HSV)
        h_bg,s_bg,v_bg = cv2.split(background)
    count += 1 

    # get frame as np array
    image = cv2.cvtColor(frame.array, cv2.COLOR_BGR2HSV)

    h,s,v = cv2.split(image)

    cv2.imshow("h",h)
    cv2.imshow("s",s)
    cv2.imshow("v",v)

    # image diff
    #diff = cv2.absdiff(background,image)
    #cv2.imshow("h diff", diff)
    ''' 
    # grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # mask
    t = cv2.getTrackbarPos("Threshold", "Adjust")
    x, mask = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(image, image, mask=mask)
    
    #cv2.imshow("background", background)
    cv2.imshow("frame", image)
    #cv2.imshow("diff", diff)
    #cv2.imshow("grayscale", gray)
    cv2.imshow("mask", mask)
    cv2.imshow("result",result)
    '''

    # escape sequence
    key = cv2.waitKey(1)
    rawCapture.truncate(0)
    if key == 27:
        break

cv2.destroyAllWindows()
