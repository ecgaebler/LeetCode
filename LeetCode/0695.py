from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
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
            matrix[y][x] = 2 #mark first cell as visited
            while queue:
                new_x, new_y = queue.popleft()
                area += 1
                for neighbor in find_neighbors(new_x, new_y, matrix):
                    queue.append(neighbor)
                    matrix[neighbor[1]][neighbor[0]] = 2 #mark cell as visited
            return area
            
        max_area = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    max_area = max(max_area, dfs(x, y, grid))
                    
        return max_area