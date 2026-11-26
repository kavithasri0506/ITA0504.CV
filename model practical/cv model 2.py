
import cv2

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    t = int(input("Enter threshold value: "))

    ret, result = cv2.threshold(
        gray, t, 255, cv2.THRESH_BINARY
    )

    cv2.imshow("Original Image", gray)
    cv2.imshow("Segmented Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
