# Subtract two images using python image library (PIL/Pillow)

import cv2
import numpy as np
from numpy import asarray
from PIL import Image, ImageChops
from time import sleep
from capture import capture # from capture.py


# simple subtraction: a-b=c, b-a=d
# very noisy results due to negative values being rounded to 0
def simple_subtract(a,b,c,d):
    
    # open imgs
    imgA = Image.open(a)
    imgB = Image.open(b)

    # convert to numpy array
    pixA = np.asarray(imgA)
    pixB = np.asarray(imgB)

    # subtract
    pixC = pixA - pixB
    pixD = pixB - pixA

    # convert back to image
    imgC = Image.fromarray(pixC)
    imgD = Image.fromarray(pixD)

    # save images
    imgC.save(c)
    imgD.save(d)

    print('saved as ' + str(c))
    print('saved as ' + str(d))


# PIL
# Outputs absolute difference to c
def abs_subtract(a,b,c,d):

    # open imgs
    imgA = Image.open(a)
    imgB = Image.open(b)
    
    # subtract
    imgC = ImageChops.subtract(imgB,imgA)
    imgD = ImageChops.subtract(imgA,imgB)

    # show and save img
    #imgC.show()
    imgC.save(c)
    imgD.save(d)
    print('saved as ' + str(c))


# PIL
# converts two RGB jpgs to grayscale, then subtracts
# Outputs absolute difference to c
def abs_subtract_gray(a,b,c):

    # open imgs
    imgA = Image.open(a).convert('L')
    imgB = Image.open(b).convert('L')
    
    # subtract
    imgC = ImageChops.subtract(imgB,imgA)

    # show and save img
    #imgC.show()
    imgC.save(c)
    print('saved as ' + str(c))



# my own subtract method that iterates pixel by pixel and
# outputs absolute difference between pixels
def slow_subtract(a,b,c):

    # open imgs
    imgA = Image.open(a)
    imgB = Image.open(b)

    width = imgA.size[0]
    height = imgA.size[1]
    arrC = np.zeros([height,width,3])

    for h in range(height):
        for w in range(width):
            pixA = imgA.getpixel((w,h))
            pixB = imgB.getpixel((w,h))
            for d in range(3):
                diff = int(abs(pixA[d]-pixB[d]))
                arrC[h,w,d] = diff
    
    # convert back to img
    imgC = Image.fromarray(np.uint8(arrC))
    #imgC.show()
    imgC.save(c)
    print('saved as ' + str(c))

# Isolate channels
# red = 0, green = 1, blue = 2
def channel(img, n):
    a = np.array(img)
    a[:,:,(n!=0, n!=1, n!=2)] *= 0
    return Image.fromarray(a)

def channeldif(img_A,img_B,n):
    A = channel(img_A,n)
    B = channel(img_B,n)
    a = asarray(A)
    b = asarray(B)
    c = a - b
    return Image.fromarray(c)

#channeldif(img_A,img_B,0).show()



a = 'a.jpg'
b = 'b.jpg'
c = 'c.jpg'
d = 'd.jpg'
e = 'e.jpg'



# Frame capture sequence
def capture_sequence():

    capture(a)
    print('static frame captured')
    print('capturing current frame in...')
    for i in range(5):
        countdown  = str(5 - i) + 's'
        print(countdown)
        sleep(1)
    capture(b)
    print('frame captured')


capture_sequence()

# This subtraction results in noisy pixels (due to negative pixels)
#simple_subtract(a,b,c,d)
    

# Use absolute difference instead
abs_subtract(a,b,c,d)

#abs_subtract_gray(a,b,c)


