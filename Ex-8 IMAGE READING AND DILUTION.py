import cv2
import numpy as np

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    dilated = cv2.dilate(gray, kernel, iterations=1)

    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
