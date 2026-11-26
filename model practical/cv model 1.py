
import cv2

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    k = int(input("Enter odd kernel size: "))

    blur = cv2.GaussianBlur(gray, (k, k), 0)

    result = cv2.hconcat([gray, blur])

    cv2.imshow("Original and Gaussian Blur", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
