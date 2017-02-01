from collections import deque
import numpy as np
import cv2

# read in the image which we took from the raspberry pi
resized_image = cv2.imread("all.jpg", 1)

# resize the image. uncomment
#height, width = resized_image.shape[:2]
#resized_image = cv2.resize(resized_image, (height, width), interpolation=cv2.INTER_CUBIC)


# here we define the range of HSV values. i.e from lower to higher

#min_green = (29, 86, 6)
#max_green = (64, 255, 255)
#min_red = (160, 100, 100)
#max_red = (179, 255, 255)
min_blue = (100, 100, 100)
max_blue = (200, 255, 255)

#you can blur the image to increase the accuracy
#blurred = cv2.GaussianBlur(resized_image, (11, 11), 0)

hsv = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

# the mask of the image with the hsv range in it
mask = cv2.inRange(hsv, min_blue, max_blue)

#you can perform some other functions of the image to increase accuracy 
#mask = cv2.erode(mask, None, iterations=0)
#mask = cv2.dilate(mask, None, iterations=0)

# finding the contours. this will be used to draw the yellow circle on the image
masked = mask.copy()
contour = cv2.findContours(masked, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

center = None

#if there are contours found, i.e the required color is present, draw a circle around it

if len(contour) >0:
    print("red found")
    c = max(contour, key=cv2.contourArea)
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    if radius > 10 :
        cv2.circle(resized_image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        cv2.circle(resized_image, center, 5, (0, 0, 255), -1)
    

# show the processed image with the circle on top
cv2.imshow("Image", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()