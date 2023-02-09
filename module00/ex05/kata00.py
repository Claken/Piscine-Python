# Put this at the top of your kata00.py file
kata = (75,45454,21)

if __name__ == '__main__':
	base_string = "The 3 numbers are: {0}, {1}, {2}"
	new_string = base_string.format(kata[0], kata[1], kata[2])
	print(new_string)