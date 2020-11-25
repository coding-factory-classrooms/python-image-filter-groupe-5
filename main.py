import cv2
import numpy as np

# Story1
img = cv2.imread("imgs/Logo_Tirna.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("outpout/Logo_Tirna_Gray.jpg", img)

# Story 2
img = cv2.imread("imgs/Logo_Tirna.jpg")
img = cv2.blur(img, (5, 5))
cv2.imwrite("outpout/Logo_Tirna_Blur.jpg", img)

# Story 3
img = cv2.imread("imgs/Logo_Tirna.jpg")
kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite("outpout/Logo_Tirna_Dilate.jpg", img)
