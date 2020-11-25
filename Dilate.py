import cv2
import numpy as np


def TransformDilate(img):
    # Story 3
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    return img
