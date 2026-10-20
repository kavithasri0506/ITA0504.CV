import cv2

img = cv2.imread(r"C:\Users\student\Documents\computer vision lab\images.jfif")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    equalized = cv2.equalizeHist(gray)

    cv2.imshow("Original Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
