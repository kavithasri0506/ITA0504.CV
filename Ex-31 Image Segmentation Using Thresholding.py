import cv2

image = cv2.imread(r"C:\Users\Admin\Downloads\computer vision lab\FACE CV.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, result = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

cv2.imshow("Original Image", gray)
cv2.imshow("Segmented Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
