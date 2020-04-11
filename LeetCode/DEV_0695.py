from collections import deque

def maxAreaOfIsland(grid):
    
    def find_neighbors(x, y, matrix):
        """ Find viable immediate neighbors of a cell """
        result = []
        if x > 0 and matrix[y][x - 1] == 1: #check left square
            result.append((x - 1, y))
        if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1: #right square
            result.append((x + 1, y))
        if y > 0 and matrix[y - 1][x] == 1: #square above
            result.append((x, y - 1))
        if y < len(matrix) - 1 and matrix[y + 1][x] == 1: #square below
            result.append((x, y + 1))
        return result
    
    def dfs(x, y, matrix):
        """ Flood fill an island and return size of island """
        area = 0
        queue = deque()
        queue.append((x, y))
        while queue:
            new_x, new_y = queue.popleft()
            matrix[new_y][new_x] = 2 #mark cell as visited
            area += 1
            for neighbor in find_neighbors(new_x, new_y, matrix):
                queue.append(neighbor)
        return area
        
    max_area = 0
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                max_area = max(max_area, dfs(x, y, grid))

    for row in grid:
        print(row)
    return max_area

test1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
test2 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(maxAreaOfIsland(test1))
print("\n\n")
print(maxAreaOfIsland(test2))
