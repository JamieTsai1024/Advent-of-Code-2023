input_file = 'input.txt'
output_file = 'output1.txt'

# Return whether the game is possible (id value) or impossible (0)
def solve(line):
    numbers = line.split(': ')[1]
    winningNumbers, elfNumbers = numbers.split(' | ')
    winningNumbers = list(map(int, winningNumbers.split()))
    elfNumbers = list(map(int, elfNumbers.split()))
    
    points = 0 
    for num in elfNumbers: 
        if num in winningNumbers: 
            if points == 0: points = 1
            else: points *= 2
    return points

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
ans = 0 

for line in input: 
    ans += solve(line.strip('\n'))

out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()