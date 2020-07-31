# Identifies objects on a static background

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
cv2.createTrackbar("Lower Bound", "Adjust", 0, 255, nothing)
cv2.createTrackbar("Upper Bound", "Adjust", 0, 255, nothing)

# Initialize camera object
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(640, 480)) # 3d array (rows,columns,colors)




# opencv uses bgr instead of rgb
# use_video_port true to treat stream as video
count = 0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    count += 1 
    # Use first few frames to get background 
    if count < 10:
        # apply gaussian blur
        background = cv2.GaussianBlur(frame.array, (5,5),0)
    else:
        # get frame as np array
        # apply gaussian blur
        image = cv2.GaussianBlur(frame.array, (5,5),0)
    
        # image diff
        diff = cv2.absdiff(image,background)
    
        # grayscale
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
        # mask
        t1 = cv2.getTrackbarPos("Lower Bound", "Adjust")
        t2 = cv2.getTrackbarPos("Upper Bound", "Adjust")
        _, mask = cv2.threshold(gray, t1, 255, cv2.THRESH_BINARY)
    
        #mask = cv2.inRange(gray, t1, t2)
    #    result = cv2.bitwise_and(image, image, mask=mask)
    
        _,contours,hierarchy = cv2.findContours(mask,1,2)
        cnt = contours[0]
        area = cv2.contourArea(cnt)
        print(area)
        x,y,w,h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(mask,(x,y),(x+w,y+h),(0,0,255),2)
    
    
    
        #cv2.imshow("background", background)
        cv2.imshow("frame", image)
        #cv2.imshow("diff", diff)
        #cv2.imshow("grayscale", gray)
        cv2.imshow("mask", rect)
    #    cv2.imshow("result",result)
    
    # escape sequence
    key = cv2.waitKey(1)
    rawCapture.truncate(0)
    if key == 27:
        break
    
cv2.destroyAllWindows()
