def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	try:
		assert len(height) == len(weight), "lists are not the same size"
		assert all((isinstance(item, int) or isinstance(item, float)) for item in height), "not the right type in the height list"
		assert all((isinstance(item, int) or isinstance(item, float)) for item in weight), "not the right type in the weight list"
	except AssertionError as e:
		print(f"{type(e).__name__}: {e}")





def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	return 42
	#your code here