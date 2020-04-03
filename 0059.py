class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        def update(matrix, x, y, direction):
            if direction == "E":
                #if you can advance in current direction...
                if x < len(matrix) - 1 and matrix[y][x + 1] == None:
                    #move into new square
                    x += 1
                    return (x, y, direction)
                #if you can't advance, try turning.
                direction = "S"
                    
            if direction == "S":
                if y < len(matrix) - 1 and matrix[y + 1][x] == None:
                    y += 1
                    return (x, y, direction)
                direction = "W"
                
            if direction == "W":
                if x > 0 and matrix[y][x - 1] == None:
                    x -= 1
                    return (x, y, direction)
                direction = "N"
                
            if direction == "N":
                if y > 0 and matrix[y - 1][x] == None:
                    y -= 1
                    return (x, y, direction)
                direction = "E"
            
            #do a final check to see if next square is open after turning from N to E
            if x < len(matrix) - 1 and matrix[y][x + 1] == None:
                x += 1
                return (x, y, direction)
            else:
                return (x, y, None)
                    
                    
        matrix = [[None]*n for _ in range(n)] #initialize empty array to be filled
        x, y, direction = 0, 0, "E"
            
        for i in range(1, n**2 + 1):
            matrix[y][x] = i
            x, y, direction = update(matrix, x, y, direction)
            if not direction:
                break
            
        return matrix
            
                