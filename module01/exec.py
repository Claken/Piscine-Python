import sys

if __name__ == '__main__' :

	joined = ""
	for elem in sys.argv:
		joined = "".join([joined, elem.swapcase()])
		joined = "".join([joined, " "])
	
	print(joined)