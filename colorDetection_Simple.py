import time
import cv2

# read the image
image = cv2.imread("all.jpg", 1)

# convert to hsv
converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


#red_lower = (160, 100, 100)
#red_upper = (179, 255, 255)

#define color code
min_blue = (100, 100, 100)
max_blue = (150, 255, 255)

# check range of converted picture versus the defined range
checked = cv2.inRange(converted, min_blue, max_blue)

# show the image
cv2.imshow("Image", checked)
cv2.waitKey(0)
cv2.destroyAllWindows()
