import cv2
import time

# Read image
img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Error: Image not found")

else:
    # Display original image
    cv2.imshow("Original Image", img)
    cv2.waitKey(2000)

    # Slow display
    cv2.imshow("Slow Motion", img)
    time.sleep(5)

    # Fast display
    cv2.imshow("Fast Motion", img)
    time.sleep(1)

    cv2.destroyAllWindows()
