import sys

if len(sys.argv) > 2:
	print("AssertionError: more than one argument is provided")
	sys.exit(1)

if len(sys.argv) != 2:
	# print("Usage: python whatis.py <number>")
	sys.exit(1)

number: int = int(sys.argv[1])

# if ValueError:
# 	print("AssertionError: argument is not an integer")
# 	sys.exit(1)

if number % 2 == 0:
	print("I'm Even")
elif number % 2 != 0:
	print("I'm Odd")
