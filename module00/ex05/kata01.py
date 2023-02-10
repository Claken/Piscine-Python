# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if __name__ == '__main__':
	base_string = "{what} was created by {who}"
	dict_list = list(kata)
	
	new_string = base_string.format(what=dict_list[0], who=kata[dict_list[0]])
	print(new_string)

	new_string = base_string.format(what=dict_list[1], who=kata[dict_list[1]])
	print(new_string)

	new_string = base_string.format(what=dict_list[2], who=kata[dict_list[2]])
	print(new_string)

