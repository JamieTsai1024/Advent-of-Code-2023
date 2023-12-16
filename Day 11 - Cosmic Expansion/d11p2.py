input_file = 'input.txt'
output_file = 'output2.txt'

def getZeroRows(grid):
    zeroRows = [] 
    for index, row in enumerate(grid): 
        if row.count('#') == 0: 
            zeroRows.append(index)
    return zeroRows 

def getZeroCols(grid):
    # Rotate clockwise 
    rotated = list(zip(*grid))[::-1]
    rotated = list(zip(*rotated))[::-1]
    rotated = list(zip(*rotated))[::-1]
    return getZeroRows(rotated) 

def getExpansion(zeros, start, end):
    return sum(1 if x > start and x < end else 0 for x in zeros)

# Return sum of "part numbers"
def solve(grid, EXPANSION_FACTOR):
    ans = 0
    galaxies = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                galaxies.append([row, col])

    zeroRows = getZeroRows(grid)
    zeroCols = getZeroCols(grid)

    for i in range(len(galaxies) - 1):
        row1, col1 = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            row2, col2 = galaxies[j]
            swappedRow = False
            swappedCol = False
            # Swap variables so `1` vars are smaller than `2` vars 
            if row1 > row2: 
                row1, row2 = row2, row1
                swappedRow = True 
            if col1 > col2: 
                col1, col2 = col2, col1
                swappedCol = True 

            # Compute answer 
            rowExpansion = getExpansion(zeroRows, row1, row2)
            colExpansion = getExpansion(zeroCols, col1, col2)
            ans += (row2 - row1) + (col2 - col1) + (rowExpansion * EXPANSION_FACTOR) + (colExpansion * EXPANSION_FACTOR)
            
            # Swap back
            if swappedRow: row1, row2 = row2, row1
            if swappedCol: col1, col2 = col2, col1
    return ans 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
grid = [] 
EXPANSION_FACTOR = 1000000 - 1
for line in input: 
    grid.append(list(line.strip('\n')))

ans = solve(grid, EXPANSION_FACTOR)
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()