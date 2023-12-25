input_file = 'input.txt'
output_file = 'output2.txt'

# Return North load
def getNorthLoad(grid): 
    totalRows = len(grid)
    load = 0 
    for row in range(len(grid)): 
        for col in range(len(grid[0])): 
            if grid[row][col] == 'O': 
                load += totalRows - row
    return load 

# Return the grid after tilting up  
def tiltGridUp(grid): 
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
    # Remove buffer of #
    del grid[0]
    return grid 

# Rotate grid 90 degrees clockwise 
def rotateClockwise(grid):  
    grid = list(zip(*grid))[::-1]
    grid = list(zip(*grid))[::-1]
    return list(list(x) for x in zip(*grid))[::-1]

# Return total load on the north support beams 
def solve(grid):
    # Upon inspection, the North load falls into a pattern with a period of 36 cycles after around 100 cycles, so we don't need to compute 1000000000 cycles 
    # 1000000000 / 36 has a remainder of 28, so we compute the North load after cycle (x * 36 + 28) = 136, where we take x = 3
    for cycle in range(136): 
        grid = tiltGridUp(grid)

        # Rotate grid so west is up 
        grid = rotateClockwise(grid)
        grid = tiltGridUp(grid)

        # Rotate grid so south is up 
        grid = rotateClockwise(grid)
        grid = tiltGridUp(grid)

        # Rotate grid so east is up 
        grid = rotateClockwise(grid)
        grid = tiltGridUp(grid)

        # Rotate grid so north is up 
        grid = rotateClockwise(grid)

        currLoad = getNorthLoad(grid)
        # print(cycle, currLoad)

    return currLoad

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