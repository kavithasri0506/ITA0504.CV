import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(r"C:\Users\student\Documents\computer vision lab\images.jfif")

    if img is None:
        print("Image not found")
        return

    colors = ('b', 'g', 'r')
    names = ('Blue', 'Green', 'Red')

    plt.figure(figsize=(8, 5))

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=names[i])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.show()

    cv2.imshow("Original Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

analyze_histogram("image.jpg")
