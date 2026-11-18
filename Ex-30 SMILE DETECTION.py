import cv2

image = cv2.imread(r"C:\Users\Admin\Downloads\computer vision lab\SMILE CV.jpg")

smile = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

smiles = smile.detectMultiScale(gray, 1.8, 20)

for (x, y, w, h) in smiles:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Smile Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
