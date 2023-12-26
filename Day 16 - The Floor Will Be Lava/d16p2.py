input_file = 'input.txt'
output_file = 'output2.txt'

# Return if x, y coordinates are in range for the grid 
def isInRange(x, y, grid): 
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

# Count the number of energized (#) tiles in the grid 
def countEnergized(grid, startBeam): 
    energized = followBeams(grid, startBeam)
    numEnergized = 0 
    for row in energized: 
        numEnergized += row.count('#')
    return numEnergized

# Return grid of energized beams
def followBeams(grid, startBeam): 
    # To detect loops, store which directions have been covered from each mirror and splitter 
    loops = [[[] for i in range(len(grid[0]))] for j in range(len(grid))] 
    energized = [['.' for i in range(len(grid[0]))] for j in range(len(grid))]
    q = [startBeam] # items: [startingPosition, direction]
    
    while q: 
        [x, y], direction = q.pop(0)

        # Skip if coordinates aren't in range 
        if not isInRange(x, y, grid):
            continue 

        # Skip if this direction has already been explored for this tile 
        if direction in loops[x][y]: 
            continue 

        # Add to loops and energized
        currTile = grid[x][y]
        loops[x][y].append(direction)
        energized[x][y] = '#'

        # Add to queue based on direction and currTile 
        if direction == 'R': 
            if currTile == '.' or currTile == '-':
                q.append([[x, y + 1], 'R'])
            elif currTile == '|':
                q.append([[x - 1, y], 'U'])
                q.append([[x + 1, y], 'D'])
            elif currTile == '/':
                q.append([[x - 1, y], 'U'])
            elif currTile == '\\':
                q.append([[x + 1, y], 'D'])
        elif direction == 'L': 
            if currTile == '.' or currTile == '-':
                q.append([[x, y - 1], 'L'])
            elif currTile == '|':
                q.append([[x - 1, y], 'U'])
                q.append([[x + 1, y], 'D'])
            elif currTile == '/':
                q.append([[x + 1, y], 'D'])
            elif currTile == '\\':
                q.append([[x - 1, y], 'U'])
        elif direction == 'U': 
            if currTile == '.' or currTile == '|':
                q.append([[x - 1, y], 'U'])
            elif currTile == '-':
                q.append([[x, y - 1], 'L'])
                q.append([[x, y + 1], 'R'])
            elif currTile == '/':
                q.append([[x, y + 1], 'R'])
            elif currTile == '\\':
                q.append([[x, y - 1], 'L'])
        elif direction == 'D': 
            if currTile == '.' or currTile == '|':
                q.append([[x + 1, y], 'D'])
            elif currTile == '-':
                q.append([[x, y - 1], 'L'])
                q.append([[x, y + 1], 'R'])
            elif currTile == '/':
                q.append([[x, y - 1], 'L'])
            elif currTile == '\\':
                q.append([[x, y + 1], 'R'])

    return energized

# Return number of energized beams 
def solve(grid):
    maxEnergized = 0 

    # Beams travelling horizontally   
    for row in range(len(grid)): 
        # Beam starting on the left column going right
        maxEnergized = max(maxEnergized, countEnergized(grid, [[row, 0], 'R']))
        # Beam starting on the right column going left 
        maxEnergized = max(maxEnergized, countEnergized(grid, [[row, len(grid[0]) - 1], 'L']))
    
    # Beams travelling vertically   
    for col in range(len(grid[0])): 
        # Beam starting on the top row going down 
        maxEnergized = max(maxEnergized, countEnergized(grid, [[0, col], 'D']))
        # Beam starting on the bottom row going up  
        maxEnergized = max(maxEnergized, countEnergized(grid, [[len(grid) - 1, col], 'U']))

    return maxEnergized

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
grid = [] 
for line in input: 
    grid.append(list(line.strip('\n')))

ans = solve(grid)
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()