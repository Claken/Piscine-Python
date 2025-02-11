def slice_me(family: list, start: int, end: int) -> list:
	
	familySize = len(family)
	elemSize = int(sum([len(elem) for elem in family]) / familySize)

	print(f"My shape is : ({familySize}, {elemSize})")

	newList = family[start:end]

	newListSize = len(newList)
	elemSize = int(sum([len(elem) for elem in newList]) / newListSize)

	print(f"My new shape is : ({newListSize}, {elemSize})")

	return newList