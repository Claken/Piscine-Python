import sys
import string

def filterwords(words):
	newwords = []
	for word in words:
		for char in word:
			if char in string.punctuation:
				word = word.replace(char, '')
		newwords.append(word)
	return newwords

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("ERROR: Invalid number of arguments")
	else:
		try:
			n = int(sys.argv[2])
		except ValueError:
			print("ERROR: argument must be an integer")
		else:
			if n > 0:
				words = sys.argv[1].split()
				words = filterwords(words)
				words = [word for word in words if len(word) > n]
				print(words)
			else:
				print("ERROR: size must be superior to zero")