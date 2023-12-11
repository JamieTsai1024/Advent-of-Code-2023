input_file = 'input.txt'
output_file = 'output2.txt'

# Return power of set of minimum cubes (r * g * b)
def solve(line):
    gameId, gameSets = line.split(': ')
    gameSets = [set.split(', ') for set in gameSets.split('; ')]
    r, g, b = 0, 0, 0
    for set in gameSets: 
        for cubes in set:
            num, colour = cubes.split(' ')
            if colour == 'red':
                r = max(r, int(num))
            elif colour == 'green':
                g = max(g, int(num))
            elif colour == 'blue': 
                b = max(b, int(num))
    return r * g * b

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