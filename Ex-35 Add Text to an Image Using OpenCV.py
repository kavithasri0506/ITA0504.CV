import cv2
import numpy as np

image = np.ones((500, 500, 3), dtype=np.uint8) * 255

cv2.putText(image, "Hello OpenCV", (80, 250),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 2)

cv2.imshow("Text on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
