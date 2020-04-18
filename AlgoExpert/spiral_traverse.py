def spiralTraverse(matrix):
	result = []
    if not matrix or not matrix[0]:
		return result
	startX, endX, startY, endY = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
	
	while startX <= endX and startY <= endY:
		for x in range(startX, endX + 1):
			result.append(matrix[startY][x])
			
		for y in range(startY + 1, endY + 1):
			result.append(matrix[y][endX])
			
		for x in reversed(range(startX, endX)):
			if startY == endY:
				break
			result.append(matrix[endY][x])
			
		for y in reversed(range(startY + 1, endY)):
			if startX == endX:
				break
			result.append(matrix[y][startX])
				
		startY += 1
		endX -= 1
		startX += 1
		endY -= 1
			
	return result
		