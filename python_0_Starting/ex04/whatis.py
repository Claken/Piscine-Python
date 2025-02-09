import sys

try:
    length: int = len(sys.argv)
    assert length < 3, "more than one argument is provided"
except AssertionError as e:
    print(f"{type(e).__name__}: {e}")

if len(sys.argv) != 2:
    sys.exit(1)

try:
    value = sys.argv[1]
    assert (
        value.isdigit()
        or (value.startswith('-') and value[1:].isdigit())
    ), "argument is not an integer"
    number = int(value)
    if number % 2 == 0:
        print("I'm Even.")
    elif number % 2 != 0:
        print("I'm Odd.")
except AssertionError as e:
    print(f"{type(e).__name__}: {e}")
