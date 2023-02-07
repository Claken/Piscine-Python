import string
import sys

def  text_analyzer(text=None):
	"""
	This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
	"""
	if text == None:
		text = input("Please type the text to analyze: \n>> ")
	elif type(text) != str:
		print("Error: this argument is not a string")

	characters = len(text)
	ups = sum(1 for c in text if c.isupper())
	lows = sum(1 for c in text if c.islower())
	spaces = sum(1 for c in text if c.isspace())
	spaces = sum(1 for c in text if c.isspace())
	punct = sum(1 for c in text if c in string.punctuation)

	print("The text contains " + str(characters) + " character(s):")
	print("- " + str(ups) + " upper letter(s)")
	print("- " + str(lows) + " lower letter(s)")
	print("- " + str(punct) + " punctuation mark(s)")
	print("- " + str(spaces) + " spaces(s)")


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Error: wrong number of arguments")
	else:
		text_analyzer(sys.argv[1])
