import cv2

img = cv2.imread(r"C:\Users\student\Documents\computer vision lab\images.jfif")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    outline = cv2.Canny(gray, 100, 200)

    cv2.imshow("Original Image", img)
    cv2.imshow("Image Outline", outline)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
