from load_image import ft_load
import cv2
from matplotlib import pyplot as plt
import numpy as np


def main():
    try:
        image_load = ft_load("animal.jpeg")
        print(image_load)
        height, width = image_load.shape[:2]
        print(height, width)
        zoom_factor = 2  # Increase detail
        center_x, center_y = width // 2, height // 2
        zoom_size_x, zoom_size_y = width // (2 * zoom_factor), height // (2 * zoom_factor)
        
        cropped = image_load[center_y - zoom_size_y:center_y + zoom_size_y, center_x - zoom_size_x:center_x + zoom_size_x]

        zoomed_image = cv2.resize(cropped, (width, height), interpolation=cv2.INTER_LINEAR)
        
        # Display the zoomed image with axes
        # plt.figure(figsize=(8, 6))
        plt.imshow(cv2.cvtColor(zoomed_image, cv2.COLOR_BGR2RGB))  # Convert to RGB for correct color display
        # plt.title("Zoomed Image")
        # plt.xlabel("X-axis (pixels)")
        # plt.ylabel("Y-axis (pixels)")
        # plt.xticks(np.linspace(0, width, num=10))
        # plt.yticks(np.linspace(0, height, num=10))
        # plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
	main()