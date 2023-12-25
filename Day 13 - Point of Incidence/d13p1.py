input_file = 'input.txt'
output_file = 'output1.txt'

# Return True if equal length arrays are equal 
def isEqual(row1, row2): 
    for i in range(len(row1)): 
        if row1[i] != row2[i]:
            return False 
    return True 

# Checks if the grid has a reflection over horizontal line mirror 
def isReflection(grid, mirror):
    for diff in range(min(mirror + 1, len(grid) - mirror - 1)):
        if not isEqual(grid[mirror - diff], grid[mirror + diff + 1]):
            return False 
    return True

def findReflectionLine(grid):
    # Reflection over a row 
    for rowMirror in range(len(grid) - 1):
        if isReflection(grid, rowMirror):
            return (rowMirror + 1) * 100 
    
    # Rotate grid 90 degrees 
    grid = list(zip(*grid))[::-1]
    grid = list(zip(*grid))[::-1]
    grid = list(zip(*grid))[::-1]

    # Reflection over a column
    for colMirror in range(len(grid) - 1):
        if isReflection(grid, colMirror):
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