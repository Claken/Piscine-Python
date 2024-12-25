import string
import sys


def text_analyzer(text=None):
    """
    This function counts the number of upper characters,
    lower characters, punctuation, spaces and digits in a given text.
    """
    if text is None:
        text = input("What is the text to count ?\n")

    characters = len(text)
    ups = sum(1 for c in text if c.isupper())
    lows = sum(1 for c in text if c.islower())
    spaces = sum(1 for c in text if c.isspace())
    spaces = sum(1 for c in text if c.isspace())
    punct = sum(1 for c in text if c in string.punctuation)
    digits = sum(1 for c in text if c.isdigit())

    print("The text contains " + str(characters) + f" character{'s' if characters > 1 else ''}:")
    print(f"- {str(ups)} upper letter{'s' if ups > 1 else ''}")
    print(f"- {str(lows)} lower letter{'s' if lows > 1 else ''}")
    print(f"- {str(punct)} punctuation mark{'s' if punct > 1 else ''}")
    print(f"- {str(spaces)} space{'s' if spaces > 1 else ''}")
    print(f"- {str(digits)} digit{'s' if digits > 1 else ''}")

if __name__ == '__main__':
	if len(sys.argv) > 2:
		print("AssertionError: wrong number of arguments")
	elif len(sys.argv) == 2:
		text_analyzer(sys.argv[1])    
	else:
		text_analyzer()