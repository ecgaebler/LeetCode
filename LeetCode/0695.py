def maxAreaOfIsland(grid):
    height, width = len(grid), len(grid[0])
    
    def find_neighbors(x, y, matrix):
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
    
    cell_ids = {} #record id for each cell
    cells_with_id = {} #record which cells have a given id
    next_id = 0
    
    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:
                neighbors = find_neighbors(x, y, grid)
                if neighbors:
                    print("cell", (x,y), "has neighbors", neighbors) #DEBUG
                    #count unique neighbor ids
                    neighbor_ids = set()
                    for cell in neighbors:
                        if cell in cell_ids: #neighbor has a registered id
                            neighbor_ids.add(cell_ids[cell])
                            print("neighbor_ids:", neighbor_ids) #DEBUG
                    if len(neighbor_ids) == 0: #no neighbors are registered
                        cell_ids[(x,y)] = next_id
                        cells_with_id[next_id] = set([(x,y)])
                        next_id += 1
                    elif len(neighbor_ids) == 1: #combine with only labeled neighbor island
                        cell_ids[(x,y)] = neighbor_ids.pop()
                        cells_with_id[cell_ids[(x,y)]].add((x,y))
                    else: #mutiple neighbors with different ids
                        combined_id = min(neighbor_ids) #choose id to keep
                        #find and relabel any neighbor islands
                        for neighbor_id in neighbor_ids:
                            if neighbor_id != combined_id:
                                #relabel cells in neighbor island
                                empty_ids = set()
                                for cell in cells_with_id[neighbor_id]:
                                    cell_ids[cell] = combined_id #change cell's id
                                    cells_with_id[combined_id].add(cell) #add to new set
                                del cells_with_id[neighbor_id] #remove now-unused id
                else: #current cell is isolated
                    cell_ids[(x,y)] = next_id
                    cells_with_id[next_id] = set([(x,y)])
                    next_id += 1

    for cell_id in cells_with_id:                           #DEBUG
        print(cell_id, "for", list(cells_with_id[cell_id])) #DEBUG

    if not cells_with_id:
        return 0
    return max(len(cells_with_id[cell_id]) for cell_id in cells_with_id)

#tests
test1 = [[1,1,0,0,0],[1,1,1,0,0],[0,0,0,1,1],[0,0,0,1,1]]
test2 = [[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[0,0,0,0,1]]
test3 = [[1,0,1],[1,1,1],[0,0,1]]
tests = [test3]
for test in tests:
    for row in test:
        print(row)
    print(maxAreaOfIsland(test))
