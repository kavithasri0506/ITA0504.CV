import cv2
import numpy as np

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
result = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original", img)
cv2.imshow("Black Hat", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
