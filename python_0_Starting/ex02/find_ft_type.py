def all_thing_is_obj(object: any) -> int:
	str = ""
	if type(object).__name__ == "str":
		str = f"{object} is in the kitchen : {type(object)}"
	elif isinstance(object, list) | isinstance(object, tuple) | isinstance(object, set) | isinstance(object, dict):
		str = type(object).__name__
		str = f"{str[0].upper()}{str[1:]} : {type(object)}"
	else:
		str = "Type not found"
	print(str)
	return 42