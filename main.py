import cv2

# Story1
img = cv2.imread("imgs/Logo_Tirna.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("outpout/Logo_Tirna_Gray.jpg", img)
