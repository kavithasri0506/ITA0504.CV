import cv2

img = cv2.imread(r"C:\Users\student\Documents\computer vision lab\images.jfif")

if img is None:
    print("Image not found")
else:
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur Image", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
