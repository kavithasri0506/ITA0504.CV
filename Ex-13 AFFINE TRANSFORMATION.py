import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\student\Documents\COMPUTER VISION lab\cv IMAGE 1.jfif")

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    matrix = cv2.getAffineTransform(pts1, pts2)

    transformed = cv2.warpAffine(img, matrix, (cols, rows))

    original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result)
    plt.title("Affine Transformed Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
