class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        num_rows = len(wall)
        min_bricks = num_rows #initialize with max possible number of bricks crossed
        edges_at = {} #dict to keep track of how many edges are at each position along the wall
        wall_width = 0
        
        #If the wall has width 1, the line most cross every brick.
        if len(wall[0]) == 1 and wall[0][0] == 1: 
            return num_rows
        
        #Count the number of edges at each relevant position along the wall.
        #We only need to record positions where there are edges.
        for row in wall:
            position = 0
            for brick in row:
                position += brick
                if position not in edges_at:
                    edges_at[position] = 0
                edges_at[position] += 1
            if wall_width == 0:
                wall_width = position
                
        for position in edges_at:
            if 0 < position < wall_width: #ignore the outside edges
                bricks_crossed = num_rows - edges_at[position]
                min_bricks = min(min_bricks, bricks_crossed)
        
        return min_bricks