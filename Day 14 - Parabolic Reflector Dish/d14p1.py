input_file = 'input.txt'
output_file = 'output1.txt'

# Return North load
def getNorthLoad(grid): 
    totalRows = len(grid)
    load = 0 
    for row in range(len(grid)): 
        for col in range(len(grid[0])): 
            if grid[row][col] == 'O': 
                load += totalRows - row
    return load 

# Return the grid after tilting north 
def tiltGridNorth(grid): 
    # Add buffer of #
    grid.insert(0, ['#'] * len(grid))
    for col in range(len(grid[0])): 
        for row in range(2, len(grid)): 
            if grid[row][col] == 'O': 
                for newRow in range(row - 1, -1, -1): 
                    if grid[newRow][col] == '#' or grid[newRow][col] == 'O': 
                        # Roll down 
                        grid[row][col] = '.'
                        grid[newRow + 1][col] = 'O'
                        break 
    # Delete buffer of #
    del grid[0]
    return grid 

# Return total load on the north support beams 
def solve(grid):
    grid = tiltGridNorth(grid)
    return getNorthLoad(grid)

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