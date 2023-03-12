import random
import sys

if __name__ == '__main__':
	if not sys.argv[1].isdigit():
		print("ERROR")
		exit()
	number = random.randint(1, 99)
	guess = int(sys.argv[1])
	if guess == number:
		print("Congratulations! You got it on your first try!")
	else:
		print("Too bad... It was", number)