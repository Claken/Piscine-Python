def all_thing_is_obj(object: any) -> int:
	str = ""
	if type(object).__name__ == "str":
		str = object + " is in the kitchen"
	else:
		str = type(object).__name__
		str = str[0].upper() + str[1:]
	print(str, ":", type(object))
	return 42