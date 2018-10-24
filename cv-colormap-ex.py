import numpy as np
import cv2

# convert image to grayscale
jeanne_gray = cv2.imread('images/bit-sm.png', cv2.IMREAD_GRAYSCALE)
jeanne_remap = cv2.applyColorMap(jeanne_gray, cv2.COLORMAP_HOT)

# use highgui to display image
cv2.imshow("Jeanne in Gray", jeanne_remap)

# keeps the image displayed
cv2.waitKey(8000)