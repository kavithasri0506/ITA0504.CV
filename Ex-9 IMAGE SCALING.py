import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Image not found")
else:
    bigger = cv2.resize(img, None, fx=2, fy=2,
                        interpolation=cv2.INTER_CUBIC)

    smaller = cv2.resize(img, None, fx=0.5, fy=0.5,
                         interpolation=cv2.INTER_AREA)

    original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    big = cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB)
    small = cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(big)
    plt.title("Bigger Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(small)
    plt.title("Smaller Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
