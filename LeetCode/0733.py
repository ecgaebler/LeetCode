from collections import deque

def floodFill(image, sr, sc, newColor):
    start_color = image[sr][sc]
    queue = deque()
    visited = set()
    queue.append( (sr, sc) )
    while queue:
        cell_row, cell_col = queue.popleft()
        if (cell_row, cell_col) not in visited:
            
            neighbors = []
            if cell_row > 0:
                neighbors.append( (cell_row - 1, cell_col) )
            if cell_row < len(image) - 1:
                neighbors.append( (cell_row + 1, cell_col) )
            if cell_col > 0:
                neighbors.append( (cell_row, cell_col - 1) )
            if cell_col < len(image[0]) - 1:
                neighbors.append( (cell_row, cell_col + 1) )
            visited.add( (cell_row, cell_col) )
            
            for neighbor_row, neighbor_col in neighbors:
                if image[neighbor_row][neighbor_col] == start_color:
                    queue.append( (neighbor_row, neighbor_col) )
        
            image[cell_row][cell_col] = newColor
            visited.add( (cell_row, cell_col) )
    
    return image
