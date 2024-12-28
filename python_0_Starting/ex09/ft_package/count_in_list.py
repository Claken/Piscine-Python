def count_in_list(lst: list, item: str) -> int:
	"""
	Count the number of  item in the list.

	:param lst: The list to count the item in.
	:param item: The item to count in the list.
	"""
	count = 0
	for i in lst:
		if i == item:
			count += 1
	return count