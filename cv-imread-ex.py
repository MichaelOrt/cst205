import numpy as np
import cv2

img = cv2.imread('images/chualar_sign.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Chular sign", img)
cv2.waitKey(7000)

# uint8
print(img.dtype)

# (3, 2, 3)
print(img.shape)
print(img)