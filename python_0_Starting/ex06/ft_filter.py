def ft_filter(function_to_apply, list_of_inputs):
	"""
    Construct an iterator from those elements of iterable for which function returns true.
    If function is None, return the items that are true.
    """
	if function_to_apply is None:
		return [x for x in list_of_inputs if x]
	return [x for x in list_of_inputs if function_to_apply(x)]