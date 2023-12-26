input_file = 'input.txt'
output_file = 'output2.txt'

# Return array of partNumbers from input of digits surrounding *  
def convertDigitsToPartNumbers(numbers, partNumbers):
    surroundingPartNumbers = [] 
    for r, c in numbers: 
        for partNumber in partNumbers: 
            row, [colStart, colEnd] = partNumber
            if row == r and colStart <= c and c <= colEnd: 
                # Ensure no overlaps 
                if not partNumber in surroundingPartNumbers: 
                    surroundingPartNumbers.append(partNumber)
    return surroundingPartNumbers

# Return sum of "part numbers"
def solve(grid):
    ans = 0 

    # Get numbers from grid 
    numbers = [] # stack of numbers, each element specifies the row number and then the start and end columns: [row, [start, end]] 
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
    # print(numbers)

    # Scan around each *
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    for row in range(len(grid)): 
        for col in range(len(grid[0])): 
            if grid[row][col] == '*': 
                surroundingDigits = [] 
                for x, y in directions: 
                    # Check in range 
                    if row + x >= 0 and row + x < len(grid) and col + y >= 0 and col + y < len(grid[0]): 
                        if grid[row + x][col + y].isdigit(): 
                            surroundingDigits.append([row + x, col + y])
                # Convert to partNumbers 
                partNumbers = convertDigitsToPartNumbers(surroundingDigits, numbers)
                print(row, col, partNumbers, 'and', surroundingDigits)
                # Compute gear ratio 
                if len(partNumbers) == 2:
                    gearRatio = 1 
                    for row, [colStart, colEnd] in partNumbers: 
                        gearRatio *= int(''.join(grid[row][colStart : colEnd + 1]))
                    ans += gearRatio

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