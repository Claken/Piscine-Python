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
	Returns a list of words from "string" that have a length greater than "integer".
	Words are separated from each other by space characters.
	:param string: The string to filter.
	:param integer: The minimum length of the words to keep.
	"""
	condition = lambda aString: len(aString) > integer
	strTab = string.split()
	return ft_filter(condition, strTab)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("AssertionError: wrong number of arguments")
		sys.exit(1)
	try:
		strToFilter = str(sys.argv[1])
		length = int(sys.argv[2])
		if (contains_special_characters(strToFilter)):
			sys.exit(1)
		print(ft_filter_string(strToFilter, length))
	except ValueError:
		print("AssertionError: the arguments are bad")
		sys.exit(1)