def moveElementToEnd(array, toMove):
    checkIndex, moveIndex = 0, len(array) - 1
	
	while checkIndex < moveIndex:
		if array[moveIndex] == toMove:
			moveIndex -= 1
		elif array[checkIndex] == toMove:
			array[checkIndex] = array[moveIndex]
			array[moveIndex] = toMove
			moveIndex -= 1
			checkIndex += 1
		else:
			checkIndex += 1
			
	return array
			