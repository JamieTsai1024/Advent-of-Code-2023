input_file = 'input.txt'
output_file = 'output1.txt'

def isSymbol(c):
    return not c.isdigit() and not c == '.'

def isPartNumber(number, grid): 
    row, [colStart, colEnd] = number 

    # check row above, including diagonals  
    if row - 1 >= 0: 
        for c in range(max(0, colStart - 1), min(colEnd + 2, len(grid[0]))): 
            charToCheck = grid[row - 1][c]
            if isSymbol(charToCheck):
                # print('YES ', end='')
                return True 
            
    # check row below, including diagonals    
    if row + 1 < len(grid):
        for c in range(max(0, colStart - 1), min(colEnd + 2, len(grid[0]))): 
            charToCheck = grid[row + 1][c]
            if isSymbol(charToCheck):
                # print('YES ', end='')
                return True 
    
    # check left
    if colStart - 1 >= 0:
        charToCheck = grid[row][colStart - 1]
        if isSymbol(charToCheck):
            # print('YES ', end='')
            return True 
    
    # check right 
    if colEnd + 1 < len(grid[0]):
        charToCheck = grid[row][colEnd + 1]
        if isSymbol(charToCheck):
            # print('YES ', end='')
            return True 
    
    # print('NO  ', end='')
    return False  

# Return sum of "part numbers"
def solve(grid):
    ans = 0 
    # print(grid)
    # stack of numbers, each element specifies the row number and then the start and end columns: [row, [start, end]] 
    numbers = [] 
    for row in range(len(grid)): 
        start = -1
        end = -1
        for col in range(len(grid[0])):
            if grid[row][col].isdigit():
                if start == -1: 
                    start = col 
                end = col 
            if start != -1 and (not grid[row][col].isdigit() or col == len(grid[0]) - 1): 
                numbers.append([row, [start, end]])
                start = -1
    print(numbers)

    # Scan around each number 
    for num in numbers: 
        row, [colStart, colEnd] = num 
        if isPartNumber(num, grid): 
            ans += int(''.join(grid[row][colStart : colEnd + 1]))
        print(row, colStart, colEnd, ''.join(grid[row][colStart : colEnd + 1]))

    return ans 

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