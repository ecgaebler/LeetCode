
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
                    print("cell", (x,y), "has neighbors", neighbors)
                    #count unique neighbor ids
                    neighbor_ids = []
                    for cell in neighbors:
                        if cell in cell_ids: #neighbor has a registered id
#                            print("current cell: ", (x,y))
#                            print("labeled neighbor found: ", cell_ids[cell], " at ", cell)
                            neighbor_ids.append(cell_ids[cell])
                    if len(neighbor_ids) == 0: #no neighbors are registered
                        cell_ids[(x,y)] = next_id
                        cells_with_id[next_id] = set([(x,y)])
                        next_id += 1
                    elif len(neighbor_ids) == 1: #combine with only labeled neighbor island
                        cell_ids[(x,y)] = neighbor_ids[0]
                        cells_with_id[neighbor_ids[0]].add((x,y))
                    else: #mutiple neighbors with different ids
                        combined_id = min(neighbor_ids) #choose id to keep
#                        print("multiple islands: ", neighbor_ids)
                        #find and relabel any neighbor islands
                        for neighbor_id in neighbor_ids:
                            if neighbor_id != combined_id:
                                #relabel cells in neighbor island
                                for cell in cells_with_id[neighbor_id]:
                                    cell_ids[cell] = combined_id #change cell's id
                                    cells_with_id[neighbor_id].discard(cell) #remove from old set
                                    cells_with_id[combined_id].add(cell) #add to new set
                                    if not cells_with_id[neighbor_id]:
                                        del cells_with_id[neighbor_id] #remove unused id 
                else: #current cell is isolated
                    cell_ids[(x,y)] = next_id
                    cells_with_id[next_id] = set([(x,y)])
                    next_id += 1

    for cell_id in cells_with_id:
        print(cell_id, "for", list(cells_with_id[cell_id]))
        
#    print(cells_with_id)
    return max(len(cells_with_id[cell_id]) for cell_id in cells_with_id)

#tests
test1 = [[1,1,0,0,0],[1,1,1,0,0],[0,0,0,1,1],[0,0,0,1,1]]
test2 = [[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0],[0,0,0,0,1]]
tests = [test1,test2]
for test in tests:
    for row in test:
        print(row)
    print(maxAreaOfIsland(test))

