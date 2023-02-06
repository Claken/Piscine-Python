import sys
import math

if __name__ == '__main__' :

	if len(sys.argv) == 2:
		try:
			number = int(sys.argv[1])
			result = math.fmod(number, 2)
			if number == 0:
				print('It is a zero')
			elif result == 1:
				print('The number is odd')
			elif result == 0:
				print('The number is even')
		except:
			print('argument is not an integer')
	if len(sys.argv) > 2:
		print("more than one argument are provided")
