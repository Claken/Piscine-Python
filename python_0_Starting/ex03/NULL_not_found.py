def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing: {object} {type(object)}")
		return 0
	elif object != object:
		print(f"Cheese: {object} {type(object)}")
		return 0
	elif isinstance(object, int) and object == 0 and object is not False:
		print(f"Zero: {object} {type(object)}")
		return 0
	elif object == "":
		print(f"Empty: {object} {type(object)}")
		return 0
	elif object is False & isinstance(object, bool):
		print(f"Fake: {object} {type(object)}")
		return 0
	else:
		print("Type not Found")
	return 1