# Subtract two images and apply a binary mask using opencv
# images are saved as jpgs

import cv2
from time import sleep
from capture import capture # from capture.py

a = 'a.jpg' # static reference frame
b = 'b.jpg' # current frame 
c = 'c.jpg' # absolute difference between static and current frame
d = 'd.jpg' # binary mask of difference
e = 'e.jpg' # contour

# Frame capture sequence
capture(a)
print('static frame captured')
print('capturing current frame in...')
for i in range(5):
    countdown  = str(5 - i) + 's'
    print(countdown)
    sleep(1)
capture(b)
print('frame captured')

# using opencv
A = cv2.imread(a)
B = cv2.imread(b)
cv2.imwrite(c,cv2.absdiff(A,B))
# convert to grayscale
gray = cv2.imread(c,0)


# threshold is 20 px
x, mask = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

_,contours,hierarchy = cv2.findContours(mask,1,2)

print(len(contours)) 
cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)
x,y,w,h = cv2.boundingRect(cnt)
mask = cv2.rectangle(mask,-1,(x,y),(x+w,y+h),(0,0,255),2)
    

cv2.imwrite(e,mask)
print("saving to " + str(e))
