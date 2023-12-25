input_file = 'input.txt'
output_file = 'output2.txt'

# Returns the number of smudges when comparing row1 and row2. If there is more than one smudge, return 2
def countOverOneSmudges(row1, row2): 
    smudges = 0
    for i in range(len(row1)): 
        if row1[i] != row2[i]:
            smudges += 1
            if smudges > 1: 
                return smudges 
    return smudges  

# Checks if the grid has a smudged reflection over horizontal line mirror 
def isSmudgedReflection(grid, mirror):
    smudges = 0
    for diff in range(min(mirror + 1, len(grid) - mirror - 1)):
        smudges += countOverOneSmudges(grid[mirror - diff], grid[mirror + diff + 1])
        if smudges > 1: 
            return False 
    return smudges == 1

def findReflectionLine(grid):
    # Reflection over a row 
    for rowMirror in range(len(grid) - 1):
        if isSmudgedReflection(grid, rowMirror):
            return (rowMirror + 1) * 100 
    
    # Rotate grid 90 degrees 
    grid = list(zip(*grid))[::-1]
    grid = list(zip(*grid))[::-1]
    grid = list(zip(*grid))[::-1]

    # Reflection over a column
    for colMirror in range(len(grid) - 1):
        if isSmudgedReflection(grid, colMirror):
            return (colMirror + 1) 
    
    # Shouldn't get here 
    return -1 

# Return cols to the left of each vertical mirror and 100 * rows above each horizontal mirror
def solve(grids):
    ans = 0 
    for grid in grids: 
        ans += findReflectionLine(grid)
    return ans 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
grids = [] 
grid = [] 
for line in input: 
    line = list(line.strip('\n'))
    if line == []: 
        grids.append(grid)
        grid = [] 
    else: 
        grid.append(line)

# Add last grid 
grids.append(grid)

ans = solve(grids)
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()