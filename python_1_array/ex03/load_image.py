import cv2
import os

def ft_load(path: str) -> list:

	try:
		image = cv2.imread(path)
		assert image is not None, "image loading has failed"
		extension = os.path.splitext(path)[1]
		assert extension == ".jpg" or extension == ".jpeg", "not the right format"
		image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		print(f"The shape of image is: {image.shape}")
		return image_rgb
	except AssertionError as e:
		print(f"{type(e).__name__}: {e}")