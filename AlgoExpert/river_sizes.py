from collections import deque
def riverSizes(matrix):
	
	def flood(matrix, river_sizes, river_id, x_pos, y_pos):
		queue = deque()
		queue.append((x_pos,y_pos))
		if not river_id in river_sizes:
			river_sizes[river_id] = 0
		while queue:
			x, y = queue.popleft()
			if matrix[y][x] != 1:
				continue
			matrix[y][x] = river_id
			river_sizes[river_id] += 1
			#check north neighbor
			if y > 0 and matrix[y - 1][x] == 1:
				queue.append((x, y - 1))
			#check east neighbor
			if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
				queue.append((x + 1, y))
			#check south neighbor
			if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
				queue.append((x, y + 1))
			#check west neighbor
			if x > 0 and matrix[y][x - 1] == 1:
				queue.append((x - 1, y))
				
    river_id = 2 #unique id for each river. Starts at 2 because matrix already uses 0 and 1.
	sizes = {} #dictionary mapping river_id to the size of that river
	for y in range(len(matrix)):
		for x in range(len(matrix[0])):
			if matrix[y][x] == 1:
				flood(matrix, sizes, river_id, x, y) #flood river, marking all connected squares
				river_id += 1
	
	result = []
	for river in sizes:
		result.append(sizes[river])
	return result