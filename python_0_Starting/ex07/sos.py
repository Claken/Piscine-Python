import sys

CHARS_TO_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}


def checkString(string):
    for char in string:
        try:
            CHARS_TO_MORSE[char]
        except KeyError:
            return False
    return True


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "wrong number of arguments"
        oneString = sys.argv[1].upper()
        assert checkString(oneString) is True, "characters must be spaces and \
alphanumeric (a-z, A-Z, 0-9)"
        for char in oneString:
            print(CHARS_TO_MORSE[char], end="")
        print("")
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
