def spiralTraverse(matrix):
	if len(matrix) == 0 or len(matrix[0]) == 0:
		return matrix
	
    def nextCell(matrix, visited, x, y, direction):
		turns = 0
		if direction == "E":
			if x < len(matrix[0]) - 1 and (x+1, y) not in visited:
				return [x+1, y, direction]
			direction = "S"
			turns += 1
		if direction == "S":
			if y < len(matrix) - 1 and (x, y+1) not in visited:
				return [x, y+1, direction]
			direction = "W"
			turns += 1
		if direction == "W":
			if x > 0 and (x-1, y) not in visited == 0:
				return [x-1, y, direction]
			direction = "N"
			turns += 1
		if direction == "N":
			if y > 0 and (x, y-1) not in visited == 0:
				return [x, y+1, direction]
			direction = "E"
			turns += 1
		if turns > 1:
			return [-1, -1, "X"]
		return [x, y, direction]
	
	x, y, direction = 0, 0, "E"
	visited = set()
	result = []
	
	while direction != "X":
		result.append(matrix[y][x])
		visited.add((x, y))
		x, y, direction = nextCell(matrix, visited, x, y, direction)
		
	return result