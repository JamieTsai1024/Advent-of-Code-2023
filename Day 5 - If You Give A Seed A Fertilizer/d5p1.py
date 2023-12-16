input_file = 'input.txt'
output_file = 'output1.txt'

# Map a source to its destination with its map 
def getDestinationFromSource(source, m):
    for dRangeStart, sRangeStart, rangeLength in m:
        if sRangeStart <= source and source < sRangeStart + rangeLength:
            source = dRangeStart + (source - sRangeStart)
            break
    return source 

# Map a seed (source) to its location (destination)  
def solve(seed, maps):
    for m in maps:
        seed = getDestinationFromSource(seed, m)
    return seed 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
ans = float('inf') # lowest location number 
maps = [[], [], [], [], [], [], []] # Maps: seed-soil, soil-fertilizer, fertilizer-water, water-light, light-temperature, temperature-humidity, humidity-location
mapIndex = -1

seeds = list(map(int, input.pop(0).replace('seeds: ', '').split()))

# Take in input and build maps 
for line in input: 
    line = line.strip('\n')
    if line == '': 
        continue 
    elif line.find(':') != -1:
        mapIndex += 1
    else:
        maps[mapIndex].append(list(map(int, line.split())))

# Find the lowest location value 
for seed in seeds: 
    locationNumber = solve(seed, maps)
    if locationNumber < ans: 
        ans = locationNumber

out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()