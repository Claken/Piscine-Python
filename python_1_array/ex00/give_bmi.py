def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""
    Calculates the Body Mass Index (BMI) for each given pair of height and weight.

    Parameters:
    ------------
    height : list[int | float]
        List of heights in meters (must contain only integers or floats).
    weight : list[int | float]
        List of weights in kilograms (must contain only integers or floats).

    Returns:
    --------
    list[int | float]
        A list containing the calculated BMI for each individual using the formula: BMI = weight / (height * height).

    """
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
	"""
    Compares each BMI value against a given limit and returns a list indicating if the BMI exceeds the limit.

    Parameters:
    ------------
    bmi : list[int | float]
        List of Body Mass Index values to analyze.
    limit : int
        Limit value to compare against the BMI values (must be an integer).

    Returns:
    --------
    list[bool]
        A list containing `True` if the corresponding BMI exceeds the limit, `False` otherwise.
    """
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