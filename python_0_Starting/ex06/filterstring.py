import sys
from ft_filter import ft_filter


def contains_special_characters(s: str) -> bool:
    """
    Check if a string contains special characters, except for spaces

    :param s: The string to check.
    """
    for char in s:
        if char.isalnum() is False and char != ' ':
            print("Error: string contains special characters")
            return True
    return False


def ft_filter_string(string: str, integer: int):
    """
    Returns a list of words from "string"
    Each word had to have a length greater than "integer".
    Words are separated from each other by space characters.

    :param string: The string to filter.
    :param integer: The minimum length of the words to keep.
    """
    def condition(aString): return len(aString) > integer
    strTab = string.split()
    return ft_filter(condition, strTab)


if __name__ == '__main__':
    try:
        assert len(sys.argv) == 3, "wrong number of arguments"
        strToFilter = str(sys.argv[1])
        assert sys.argv[2].isdigit(), "second argument is not an integer"
        length = int(sys.argv[2])
        if (contains_special_characters(strToFilter)):
            sys.exit(1)
        print(ft_filter_string(strToFilter, length))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
