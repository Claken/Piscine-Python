import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
	
	
	elemSize = np.mean([len(elem) for elem in family])

	print(f"My shape is : ({len(family)}, {elemSize})")

	newList = family[start:end]

	elemSize = int(np.mean([len(elem) for elem in newList]))

	print(f"My new shape is : ({len(newList)}, {elemSize})")

	return newList