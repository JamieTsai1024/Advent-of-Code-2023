input_file = 'input.txt'
output_file = 'output1.txt'

# Find calibration value for a line 
def solve(line):
    first = -1
    last = -1 
    for i in line: 
        if i.isdigit():
            if first == -1: 
                first = int(i)
            last = int(i)
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