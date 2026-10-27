import cv2
import numpy as np

img = cv2.imread(r"C:\Users\student\Documents\computer vision lab\images.jfif")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    eroded = cv2.erode(gray, kernel, iterations=1)

    cv2.imshow("Original Image", img)
    cv2.imshow("Eroded Image", eroded)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
