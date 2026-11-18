import cv2

image = cv2.imread(r"C:\Users\Admin\Downloads\computer vision lab\FACE CV.jpg")

eye = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eyes = eye.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Eye Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
