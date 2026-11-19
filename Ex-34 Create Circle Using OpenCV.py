import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255

cv2.circle(image, (width//2, height//2), 80, (0, 0, 255), 3)

cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
