def ft_tqdm(lst: range) -> None:
	"""
	
	"""
	maxSize = len(lst)
	for elem in lst:
		print(f"{elem}/{maxSize}")
		yield elem
    #your code here