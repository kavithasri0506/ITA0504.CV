import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255

w = width // 10
h = height // 10

image[0:h, 0:w] = (0, 0, 0)
image[0:h, width-w:width] = (255, 0, 0)
image[height-h:height, 0:w] = (0, 255, 0)
image[height-h:height, width-w:width] = (0, 0, 255)

cv2.imshow("Colored Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
