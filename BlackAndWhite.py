import cv2
import os


def TransformNetB(img):
    # Story1
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
