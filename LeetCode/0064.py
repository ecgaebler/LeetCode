class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if x > 0:
                    if y > 0:
                        grid[y][x] += min(grid[y-1][x], grid[y][x-1])
                    else:
                        grid[y][x] += grid[y][x-1]
                else:
                    if y > 0:
                        grid[y][x] += grid[y-1][x]
        return grid[-1][-1]