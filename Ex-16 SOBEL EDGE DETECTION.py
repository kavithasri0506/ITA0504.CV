import cv2

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

x = cv2.convertScaleAbs(x)
y = cv2.convertScaleAbs(y)

result = cv2.addWeighted(x, 0.5, y, 0.5, 0)

cv2.imshow("Sobel X", x)
cv2.imshow("Sobel Y", y)
cv2.imshow("Sobel Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
