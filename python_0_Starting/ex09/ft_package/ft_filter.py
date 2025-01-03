def ft_filter(function_to_apply, list_of_inputs):
    """
    Construct an iterator from list_of_inputs for which function returns true.
    If function is None, return the items that are true.

    :param function_to_apply: The function that returns a boolean value.
    :param list_of_inputs: The list of elements to filter.
    """
    if function_to_apply is None:
        return [x for x in list_of_inputs if x]
    return [x for x in list_of_inputs if function_to_apply(x)]
