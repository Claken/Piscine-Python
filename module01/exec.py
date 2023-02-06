import sys

if __name__ == '__main__' :

	if len(sys.argv) > 1:
		joined = ""
		sys.argv.reverse()

		for elem in sys.argv:
			if elem != "exec.py":
				elem = elem.swapcase()
				for letter in reversed(elem):
					joined = "".join([joined, letter])
				if elem.swapcase() != sys.argv[len(sys.argv) - 2]:
					joined = "".join([joined, " "])
		print(joined)