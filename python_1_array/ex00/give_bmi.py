def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculates the Body Mass Index for each given pair of height and weight.

    Parameters:
    ------------
    height : list[int | float]
        List of heights in meters (must contain only integers or floats).
    weight : list[int | float]
        List of weights in kilograms (must contain only integers or floats).

    Returns:
    --------
    list[int | float]
        A list containing the BMI for each element using the formula:
        BMI = weight / (height * height).
    """
    try:
        assert len(height) == len(weight), "lists are not the same size"
        hei = all((isinstance(i, int) or isinstance(i, float)) for i in height)
        assert hei, "not the right type in the height list"
        wei = all((isinstance(i, int) or isinstance(i, float)) for i in weight)
        assert wei, "not the right type in the weight list"
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
    Compares each BMI value against a given limit
    Returns a list indicating if the BMI exceeds the limit.

    Parameters:
    ------------
    bmi : list[int | float]
        List of Body Mass Index values to analyze.
    limit : int
        Limit value to compare against the BMI values (must be an integer).

    Returns:
    --------
    list[bool]
        A list containing `True` if the corresponding BMI exceeds the limit
        Otherwise: `False`.
    """
    try:
        typ = all((isinstance(i, int) or isinstance(i, float)) for i in bmi)
        assert typ, "not the right type"
        assert type(limit).__name__ == "int", 'not the right type for limit'
        limit_list: list[bool] = [False] * len(bmi)
        i: int = 0
        for elem in bmi:
            if elem > limit:
                limit_list[i] = True
            i = i + 1
        return limit_list
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
