import cv2
import numpy as np


def TransformDilate():
    # Story 3
    img = cv2.imread("imgs/Logo_Tirna.jpg")
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite("output/Logo_Tirna_Dilate.jpg", img)
