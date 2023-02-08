import sys
import math

if __name__ == '__main__' :
	if len(sys.argv) <= 1:
		print("""
		Usage: python operations.py <number1> <number2>
		Example:
		python operations.py 10 3
		""")
	elif len(sys.argv) != 3:
		print("You need TWO integers")
	else:
		try:
			integer01 = int(sys.argv[1])
		except:
			print('The first argument is not an integer')
		try:
			integer02 = int(sys.argv[2])
		except:
			print('The second argument is not an integer')
		else:
			add = integer01 + integer02
			min = integer01 - integer02
			tim = integer01 * integer02
			div = integer01 / integer02
			mod = integer01 % integer02
			print("Sum       : " + str(add))
			print("Difference: " + str(min))
			print("Product   : " + str(tim))
			print("Quotient  : " + str(div))
			print("Remainer  : " + str(mod))

