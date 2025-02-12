import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        listLen = len(family[0])
        assert type(family).__name__ == "list", "no list provided"
        assert type(start).__name__ == "int", "not an int for start"
        assert type(end).__name__ == "int", "not an int for end"
        assert all(len(e) == listLen for e in family), "lists don't have the same size"
        elemSize = int(np.mean([len(elem) for elem in family]))
        print(f"My shape is : ({len(family)}, {elemSize})")
        newList = family[start:end]
        elemSize = int(np.mean([len(elem) for elem in newList]))
        print(f"My new shape is : ({len(newList)}, {elemSize})")
        return newList
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
