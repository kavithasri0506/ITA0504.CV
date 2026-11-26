import cv2

cap = cv2.VideoCapture(r"C:\Users\student\Videos\Ex-28 vehicle detection.mp4")
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

frames.reverse()

height, width, _ = frames[0].shape

out = cv2.VideoWriter(
    "reverse.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    20,
    (width, height)
)

for frame in frames:
    out.write(frame)

out.release()
print("Reverse video saved successfully")
