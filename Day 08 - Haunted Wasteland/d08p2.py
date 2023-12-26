from math import gcd

input_file = 'input.txt'
output_file = 'output2.txt'

# Return the lcm of a and b
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Returns steps to end from currLocation
def stepsToEnd(currLocation, directions, maps):
    steps = 0 
    index = 0 
    while currLocation[-1] != 'Z':
        map = maps[currLocation]
        currLocation = map[0] if directions[index] == 'L' else map[1]
        steps += 1 
        index += 1 
        index %= len(directions)
    return steps 

# Return total steps to reach the end 
def solve(directions, maps):
    steps = 1
    # Compute lcm of all times to reach Z
    for start in maps.keys():
        if start[-1] == 'A': 
            # For each starting point, compute time to get to Z
            time = stepsToEnd(start, directions, maps)
            # Take the lcm of time and the total steps to find how many total steps are required   
            steps = lcm(steps, time)
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

# print(maps)
ans = solve(directions, maps)
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()