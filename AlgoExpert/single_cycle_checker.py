def hasSingleCycle(array):
    n = len(array)
	i = 0
	numjumps = 0
	while numjumps < n:
		if numjumps > 0 and i == 0:
			return False
		i = i + array[i]
		while i < 0:
			i += len(array)
		while i >= len(array):
			i -= len(array)
		numjumps += 1
	return i == 0