import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    pts2 = np.float32([
        [50, 50],
        [cols - 50, 0],
        [0, rows - 50],
        [cols - 100, rows - 100]
    ])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    transformed = cv2.warpPerspective(img, matrix, (cols, rows))

    original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.title("Perspective Transformed Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
