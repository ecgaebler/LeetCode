def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	elif len(array) < 3:
		return max(array)
	
    back2, back1 = array[0], max(array[1], array[0])
	for idx in range(2, len(array)):		
		current_max = max(back1, array[idx] + back2)
		back2 = back1
		back1 = current_max

	return current_max