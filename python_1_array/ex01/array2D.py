import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a list of equally sized sublists.

    This function validates that the given `family` is a list of sublists
    where each sublist has the same length. It then slices the list using
    the provided start and end indices, prints the shape of the original
    and the sliced list, and returns the sliced list.

    Parameters:
        family (list): A list of sublists. Each sublist must have the same
            length.
        start (int): The starting index from which to slice the list.
        end (int): The ending index (exclusive) up to which to slice the list.

    Returns:
        list: The sliced portion of the original list, containing sublists
        from index `start` to `end - 1`.
    """
    try:
        listLen = len(family[0])
        assert type(family).__name__ == "list", "no list provided"
        assert type(start).__name__ == "int", "not an int for start"
        assert type(end).__name__ == "int", "not an int for end"
        sameSize = all(len(e) == listLen for e in family)
        assert sameSize, "lists don't have the same size"
        elemSize = int(np.mean([len(elem) for elem in family]))
        print(f"My shape is : ({len(family)}, {elemSize})")
        newList = family[start:end]
        elemSize = int(np.mean([len(elem) for elem in newList]))
        print(f"My new shape is : ({len(newList)}, {elemSize})")
        return newList
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
