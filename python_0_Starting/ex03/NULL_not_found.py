def NULL_not_found(object: any) -> int:
	if object is None or object is float("NaN") or object is 0 or object is "" or object is False:
		print(f"{object}: {object} {type(object)}")
		return 0
	else:
		print("Type not Found")
	return 1