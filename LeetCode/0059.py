class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [ [[] for _ in range(n)] for _ in range(n) ]
        y_start, y_end = 0, n 
        x_start, x_end = 0, n
        counter = 1
        while y_start < y_end and x_start < x_end:
            for x in range(x_start, x_end): #top side
                result[y_start][x] = counter
                counter += 1
            for y in range(y_start + 1, y_end): #right side
                result[y][x_end - 1] = counter
                counter += 1
            for x in range(x_end - 2, x_start - 1, -1): #bottom side
                result[y_end - 1][x] = counter
                counter += 1
            for y in range(y_end - 2, y_start, -1): #left side
                result[y][x_start] = counter
                counter += 1
            y_start += 1
            y_end -= 1
            x_start += 1
            x_end -= 1
        return result
                