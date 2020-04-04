from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #catch edge case with empty arrays
        if len(grid) == 0 or len(grid[0]) == 0: 
            return 0
        
        height = len(grid)
        width = len(grid[0])
        
        #function for flooding an island and erasing all land tiles in it
        def flood(grid, x, y):
            if y in range(len(grid)) and x in range(len(grid[0])) and grid[y][x] == "1":
                grid[y][x] = "0"
                flood(grid, x-1, y)
                flood(grid, x+1, y)
                flood(grid, x, y-1)
                flood(grid, x, y+1)  
        
        #loop through all elements in the grid, flooding islands as they are found
        islands = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1":
                    islands += 1
                    flood(grid, x, y)
                    
        return islands 