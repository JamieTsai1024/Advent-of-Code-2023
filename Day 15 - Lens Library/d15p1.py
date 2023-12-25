input_file = 'input.txt'
output_file = 'output1.txt'

# Return value of HASH algorithm applied to string s
def hash(s): 
    hashValue = 0 
    for i in range(len(s)): 
        hashValue += ord(s[i])
        hashValue *= 17
        hashValue %= 256
    return hashValue

# Return sum of HASH values 
def solve(initializationSequence):
    ans = 0
    for s in initializationSequence:
        ans += hash(s) 
    return ans 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
initializationSequence = list(input.pop(0).split(','))

ans = solve(initializationSequence)

out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()