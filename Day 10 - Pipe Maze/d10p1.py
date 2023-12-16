input_file = 'input.txt'
output_file = 'output1.txt'

def goN(c):
    return c in ['|', '7', 'F']
def goS(c):
    return c in ['|', 'L', 'J']
def goE(c):
    return c in ['-', '7', 'J']
def goW(c):
    return c in ['-', 'L', 'F']

def getStartingCharacterAndDirection(grid, currLocation): 
    row, col = currLocation 
    directions = []

    # Check north 
    if row > 0: 
        if goN(grid[row - 1][col]):
            directions.append('N')
    # Check soUth  
    if row < len(grid) - 2: 
        if goS(grid[row + 1][col]):
            directions.append('S')
    # Check west   
    if col > 0: 
        if goW(grid[row][col - 1]):
            directions.append('W')
    # Check east   
    if col < len(grid[0]) - 2: 
        if goE(grid[row][col + 1]):
            directions.append('E')
    
    if directions == ['N', 'S']:
        return ['|', 'S'] # prevDirection should be opposite of one of the directions 
    if directions == ['N', 'W']:
        return ['J', 'S']
    if directions == ['N', 'E']:
        return ['W', 'S']
    if directions == ['S', 'E']:
        return ['F', 'N']
    if directions == ['S', 'W']:
        return ['7', 'N']
    if directions == ['W', 'E']:
        return ['-', 'E']

def getNextPosition(grid, currLocation, prevDirection): 
    row, col = currLocation 
    currChar = grid[row][col]

    checkN = False
    checkS = False
    checkE = False
    checkW = False

    if goN(currChar): 
        checkS = True 
    if goS(currChar):
        checkN = True  
    if goE(currChar): 
        checkW = True 
    if goW(currChar):
        checkE = True 
        
    # Move up 
    if checkN and prevDirection != 'S': 
        return [[row - 1, col], 'N']
    if checkS and prevDirection != 'N': 
        return [[row + 1, col], 'S']
    if checkE and prevDirection != 'W': 
        return [[row, col + 1], 'E']
    if checkW and prevDirection != 'E': 
        return [[row, col - 1], 'W']

    return [2, 0]

# Return max distance away from start in cycle 
def solve(grid, start):
    ans = 1
    startingChar, prevDirection = getStartingCharacterAndDirection(grid, start)
    row, col = start
    grid[row][col] = startingChar
    tort, prevDirectionT = getNextPosition(grid, start, prevDirection)
    hare, prevDirectionH = getNextPosition(grid, start, prevDirection)
    hare, prevDirectionH = getNextPosition(grid, hare, prevDirectionH)

    while hare != start:
        # Hare moves twice as fast as tortoise
        # Note: hare must take an even number of steps to get back to the start  
        ans += 1
        tort, prevDirectionT = getNextPosition(grid, tort, prevDirectionT)
        hare, prevDirectionH = getNextPosition(grid, hare, prevDirectionH)
        hare, prevDirectionH = getNextPosition(grid, hare, prevDirectionH)

    return ans 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
grid = [] 
start = []
for line in input: 
    grid.append(list(line.strip('\n')))
    if start == [] and 'S' in grid[-1]: 
        start = [len(grid) - 1, grid[-1].index('S')]

ans = solve(grid, start)
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()