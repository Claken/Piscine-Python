import string
import sys


def text_analyzer(text=None):
    """
    This function counts the number of upper characters,
    lower characters, punctuation, spaces and digits in a given text.
    """
    if text is None:
        text = input("What is the text to count ?\n")
    elif type(text) != str:
        print("Error: this argument is not a string")

    characters = len(text)
    ups = sum(1 for c in text if c.isupper())
    lows = sum(1 for c in text if c.islower())
    spaces = sum(1 for c in text if c.isspace())
    spaces = sum(1 for c in text if c.isspace())
    punct = sum(1 for c in text if c in string.punctuation)
    digits = sum(1 for c in text if c.isdigit())

    print("The text contains " + str(characters) + " character(s):")
    print("- " + str(ups) + " upper letter(s)")
    print("- " + str(lows) + " lower letter(s)")
    print("- " + str(punct) + " punctuation mark(s)")
    print("- " + str(spaces) + " spaces(s)")
    print("- " + str(digits) + " digit(s)")


if __name__ == '__main__':
	if len(sys.argv) > 2:
		print("AssertionError: wrong number of arguments")
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])    
	else:
		text_analyzer()