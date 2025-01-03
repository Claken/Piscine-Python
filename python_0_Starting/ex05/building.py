import string
import sys


def text_analyzer(text=None):

    """
    This function counts the number of upper characters,
    lower characters, punctuation, spaces and digits in a given text.
    if text is None, the user is prompted to enter a text.

    :param text: The text to analyze.
    """
    if text is None:
        print("What is the text to count?")
        text = sys.stdin.readline()

    characters = len(text)
    ups = sum(1 for c in text if c.isupper())
    lows = sum(1 for c in text if c.islower())
    spaces = sum(1 for c in text if c.isspace())
    spaces = sum(1 for c in text if c.isspace())
    punct = sum(1 for c in text if c in string.punctuation)
    digits = sum(1 for c in text if c.isdigit())

    plural = 's' if characters > 1 else ''
    print(f"The text contains {str(characters)} character{plural}:")
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
