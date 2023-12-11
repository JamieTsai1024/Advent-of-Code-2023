input_file = 'input.txt'
output_file = 'output2.txt'

# Find calibration value for a line 
def solve(line):
    first = -1
    last = -1
    # Maps words with digits 
    wordDigits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    for i in range(len(line)): 
        for word in wordDigits: 
            if line[i:i+len(word)] == word: 
                if first == -1: 
                    first = wordDigits[word]
                last = wordDigits[word]
        if line[i].isdigit():
            if first == -1: 
                first = int(line[i])
            last = int(line[i])

    # print(first * 10 + last)
    return first * 10 + last 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
ans = 0 

for line in input: 
    ans += solve(line)

out_file.write(str(ans))

# Close files 
in_file.close()
out_file.close()