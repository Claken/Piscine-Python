from PIL import Image
import numpy as np

def ft_load(path: str) -> list:

	image = Image.open(path)
	image.show()

	image_array = np.array(image)
	print(image_array.shape)