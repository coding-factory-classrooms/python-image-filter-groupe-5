import cv2

#Story1
img = cv2.imread("Logo_Tirna.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("tot.jpg", img)
