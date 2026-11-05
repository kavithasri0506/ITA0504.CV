import cv2
import numpy as np

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)
result = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original", img)
cv2.imshow("Closing", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
