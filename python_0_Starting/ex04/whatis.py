import sys

if len(sys.argv) > 2:
	print("AssertionError: more than one argument is provided")
	sys.exit(1)

if len(sys.argv) != 2:
	sys.exit(1)

try:
    number: int = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

if number % 2 == 0:
	print("I'm Even")
elif number % 2 != 0:
	print("I'm Odd")
