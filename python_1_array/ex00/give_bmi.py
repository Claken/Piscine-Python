def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	try:
		assert len(height) == len(weight), "lists are not the same size"
		assert all((isinstance(item, int) or isinstance(item, float)) for item in height), "not the right type in the height list"
		assert all((isinstance(item, int) or isinstance(item, float)) for item in weight), "not the right type in the weight list"
		bmi_list: list[int | float] = [0] * len(height)
		i: int = 0
		for w, h in zip(weight, height):
			bmi_list[i] = w / (h * h)
			i = i + 1
		return bmi_list
	except AssertionError as e:
		print(f"{type(e).__name__}: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	try:
		assert all((isinstance(item, int) or isinstance(item, float)) for item in bmi), "not the right type"
		assert type(limit) == int, 'not the right type for the limit'
		limit_list: list[bool] = [False] * len(bmi)
		i: int = 0
		for elem in bmi:
			if elem > limit:
				limit_list[i] = True
			i = i + 1
		return limit_list
	except AssertionError as e:
		print(f"{type(e).__name__}: {e}")