input_file = 'input.txt'
output_file = 'output1.txt'

# Return steps to reach the end 
def solve(directions, maps):
    steps = 0 
    index = 0 
    currLocation = 'AAA'
    while currLocation != 'ZZZ':
        map = maps[currLocation]
        currLocation = map[0] if directions[index] == 'L' else map[1]
        steps += 1 
        index += 1 
        index %= len(directions)
    return steps 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
ans = 0 
maps = {}
directions = input.pop(0).strip('\n')
input.pop(0) # Discard empty line

# Build map
for line in input: 
    line = line.strip('\n')
    start, destination = line.split(' = ')
    left, right = destination.replace('(', '').replace(')', '').split(', ')
    maps[start] = [left, right]

ans = solve(directions, maps)
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()