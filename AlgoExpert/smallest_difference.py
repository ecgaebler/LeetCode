from sys import maxsize
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	leastDiff, leastPair = float("inf"), [0, 0]
	idx1, idx2 = 0, 0
	
	while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
		currentDiff = abs(arrayOne[idx1] - arrayTwo[idx2])
		if currentDiff == 0:
			return [arrayOne[idx1], arrayTwo[idx2]]
		else:
			if currentDiff < leastDiff:
				leastDiff = currentDiff
				leastPair = [idx1, idx2]
			if arrayOne[idx1] < arrayTwo[idx2]:
				idx1 += 1
			else:
				idx2 += 1
				
	return [arrayOne[leastPair[0]], arrayTwo[leastPair[1]]]