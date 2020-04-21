def kadanesAlgorithm(array):
    max_here = float("-inf")
	max_total = float("-inf")
	for i in range(len(array)):
		if array[i] > max_here + array[i]:
			max_here = array[i]
		else:
			max_here = max_here + array[i]
		max_total = max(max_total, max_here)
	return max_total
	