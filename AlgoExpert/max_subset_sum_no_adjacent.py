#input: 7, 10, 12, 7, 9, 14
def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	elif len(array) < 3:
		return max(array)
	
    max_after = {0:array[0], 1:max(array[1], array[0])}
	for idx in range(2, len(array)):
		max_after[idx] = max(max_after[idx - 1], array[idx] + max_after[idx - 2])
	return max_after[(len(array) - 1)]