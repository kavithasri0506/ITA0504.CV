import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Image not found")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.title("270 Degree Clockwise Rotation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
