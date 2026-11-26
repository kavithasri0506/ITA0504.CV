
import cv2

cap = cv2.VideoCapture(r"C:\Users\student\Downloads\Cars_driving_at_night.webm")

bg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    mask = bg.apply(frame)

    contours, h = cv2.findContours(
        mask, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contours:
        area = cv2.contourArea(c)

        if area > 500:
            x, y, w, h = cv2.boundingRect(c)

            cv2.rectangle(frame, (x, y),
                          (x+w, y+h), (0, 255, 0), 2)

            cv2.putText(frame, "Vehicle",
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
