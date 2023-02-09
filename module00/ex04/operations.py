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
		print("Error: You need TWO integers")
	else:
		try:
			integer01 = int(sys.argv[1])
			integer02 = int(sys.argv[2])
		except:
			print('Error: only integers are valid arguments')
		else:
			add = integer01 + integer02
			min = integer01 - integer02
			tim = integer01 * integer02
			print("Sum       : " + str(add))
			print("Difference: " + str(min))
			print("Product   : " + str(tim))
			if integer02 != 0:
				div = integer01 / integer02
				mod = integer01 % integer02
			print("Quotient  : " + (str(div) if integer02 != 0 else "ERROR (division by zero)"))
			print("Remainer  : " + (str(mod) if integer02 != 0 else "ERROR (modulo by zero)"))

