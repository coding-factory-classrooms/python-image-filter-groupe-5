import cv2
import os


def TransformNetB():
    # Story1
    img = cv2.imread("imgs/Logo_Tirna.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("output/Logo_Tirna_Gray.jpg", img)
