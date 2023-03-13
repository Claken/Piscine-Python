import random
import sys

if __name__ == '__main__':
	print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!
""")
	number = random.randint(1, 99)
	attempts = 1
	while 1:
		guess = input("What's your guess between 1 and 99?\n>> ")
		if guess == "exit":
			print("Goodbye!")
			exit()
		if guess == "" or not guess.isdigit():
			print("That's not a number.")
			continue
		guess = int(guess)
		if guess == number:
			if number == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if attempts == 1:
				print("Congratulations! You won on your first try!")
			else:
				print("Congratulations! You won in {} attempt.s!".format(attempts))
			exit()
		elif guess > number:
			print("Too high!")
		elif guess < number:
			print("Too low!")
		attempts = attempts + 1