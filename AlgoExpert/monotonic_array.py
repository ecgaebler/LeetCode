def isMonotonic(array):
	if len(array) < 2:
		return True
    direction = 0
	
	for i in range(len(array) - 1):
		if array[i] < array[i+1]: #positive slope
			if direction == 0:
				direction = 1
			elif direction < 0:
				return False
		elif array[i] > array[i+1]: #negative slope
			if direction == 0:
				direction = -1
			elif direction > 0:
				return False
			
	return True