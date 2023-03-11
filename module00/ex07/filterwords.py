import sys
import string

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR: Invalid number of arguments")
	else:
		try:
			n = int(sys.argv[2])
		except ValueError:
			print("ERROR: Invalid argument")
		else:
			if n > 0:
				words = sys.argv[1].split()
				words = [word for word in words if len(word) > n]

				print(words)
			else:
				print("ERROR: size must be superior to zero")