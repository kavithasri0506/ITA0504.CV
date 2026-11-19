import cv2
import numpy as np

image = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if image is None:
    print("Image not found")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([0, 50, 50])
upper = np.array([10, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

foreground = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Foreground", foreground)

cv2.waitKey(0)
cv2.destroyAllWindows()
