def find_max_min(list_in):
	try:
		max_item = max(list_in)
		min_item = min(list_in)
		if max_item != min_item:
			return [min_item, max_item]
		else:
			return len(list_in)
	except Exception:
		return 'invalid'

print find_max_min([4,4,4,4,4])