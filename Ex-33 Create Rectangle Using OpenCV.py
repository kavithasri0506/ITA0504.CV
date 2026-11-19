import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255

cv2.rectangle(image, (50, 50), (200, 150), (0, 0, 255), 3)

cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
