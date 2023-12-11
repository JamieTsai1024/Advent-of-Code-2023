from math import ceil, sqrt

input_file = 'input.txt'
output_file = 'output1.txt'

# Return number of ways to beat the record 
def solve(time, distance):
    # Let x be the time we hold the button, t be the time, and d be the distance
    # Then, we want x(t-x) > d, or x^2 - tx + d < 0
    # Using the quadratic formula, we have (t - sqrt(t^2 - 4d)) / 2 < x < (t + sqrt(t^2 - 4d)) / 2
    lowerBound = (time - sqrt(time ** 2 - 4 * distance)) / 2
    upperBound = (time + sqrt(time ** 2 - 4 * distance)) / 2

    # Round lowerbound
    if int(lowerBound) == lowerBound: 
        lowerBound += 1 # integer - add 1 
    else: 
        lowerBound = ceil(lowerBound) # decimal - round up 

    # Round upperbound
    if int(upperBound) == upperBound: 
        upperBound -= 1 # integer - subtract 1 
    else: 
        upperBound //= 1 # decimal - round down 

    return int(upperBound - lowerBound + 1) 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
ans = 1
times = list(map(int, input.pop(0).replace('Time: ', '').split()))
distances = list(map(int, input.pop(0).replace('Distance: ', '').split()))

for i in range(len(times)): 
    ans *= solve(times[i], distances[i])

out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()