input_file = 'input.txt'
output_file = 'output1.txt'

# Return whether the game is possible (id value) or impossible (0)
def solve(line):
    gameId, counts = line.split(': ')
    gameNumber = int(gameId.split(' ')[1])
    counts = [item.split(', ') for item in counts.split('; ')]
    # print(gameNumber, counts)
    for set in counts: 
        r, g, b = 0, 0, 0
        for cubes in set:
            num, colour = cubes.split(' ')
            if colour == 'red':
                r += int(num)
                if r > 12: return 0
            elif colour == 'green':
                g += int(num)
                if g > 13: return 0
            elif colour == 'blue': 
                b += int(num)
                if b > 14: return 0
    return gameNumber

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