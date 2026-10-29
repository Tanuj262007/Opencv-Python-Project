#CHANNEL --> 0 TO 255

import cv2
import numpy as np

img = cv2.imread("C:/Users/Deepak/PycharmProjects/OPENCV/images/highway.jpeg")

if img is None:
    print("Image not found. Check the file path.")
    exit()

threshold_value = 100

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary_threshold = cv2.threshold(
    gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Original", img)
cv2.imshow("Binary Threshold", binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
