import cv2

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

roi = img[50:200, 50:200]
copy = roi.copy()

img[200:350, 200:350] = copy

cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
