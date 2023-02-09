# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if __name__ == '__main__':
	base_string_0 = "{what} was created by {}"
	new_string = base_string_0.format()
	print(new_string)