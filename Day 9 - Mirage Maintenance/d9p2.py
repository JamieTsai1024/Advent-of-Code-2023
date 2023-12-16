input_file = 'input.txt'
output_file = 'output2.txt'

# Return next value from history 
def solve(history):
    history = history[::-1]
    # print(history)
    steps = [[history[0]]]

    # Build tree 
    for i in range(1, len(history)):
        steps[0].append(history[i])
        # if steps[i-1] == [0] * len(steps[i-1]): 
        #     break 
        steps.append([])
        for row in range(1, len(steps)): 
            steps[row].append(steps[row-1][-2] - steps[row-1][-1])
            # if steps[row][-1] == 0: 
            #     break
        # print('i', i, steps)
        # if steps[-1][0] == 0: 
        #     break 
    # print(steps)
    # Construct previous value 
    for i in range(len(steps) - 2, -1, -1): 
        steps[i].append(steps[i][-1] - steps[i+1][-1])
    # print(steps)
    return steps[0][0]

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
ans = 0 

for line in input: 
    ans += solve(list(map(int, line.strip('\n').split(' '))))

out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()