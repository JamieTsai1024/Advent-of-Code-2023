input_file = 'input.txt'
output_file = 'output2.txt'

# Return value of HASH algorithm applied to string s
def hash(s): 
    hashValue = 0 
    for i in range(len(s)): 
        hashValue += ord(s[i])
        hashValue *= 17
        hashValue %= 256
    return hashValue

# Operate on hashmap based on - or = direction 
def followDirection(direction, hashMap):
    if direction.find('-') != -1: 
        # Remove label 
        label = direction[:-1]
        hashValue = hash(label)
        for slot in range(len(hashMap[hashValue])):
            if hashMap[hashValue][slot][0] == label: 
                del hashMap[hashValue][slot]
                return hashMap
    else:
        # Add/update label 
        label, focalLength = direction.split('=')
        hashValue = hash(label)
        focalLength = int(focalLength)
        # Update label 
        for slot in range(len(hashMap[hashValue])): 
            if hashMap[hashValue][slot][0] == label: 
                hashMap[hashValue][slot][1] = focalLength
                return hashMap 
        # Add label if it doesn't exist 
        hashMap[hashValue].append([label, focalLength])
    return hashMap 

def buildHashMap(initializationSequence): 
    hashMap = [[] for i in range(256)] 
    for direction in initializationSequence: 
        hashMap = followDirection(direction, hashMap)
    return hashMap

# Return sum of HASH values 
def solve(initializationSequence):
    hashMap = buildHashMap(initializationSequence)
    ans = 0
    for hashIndex, lenses in enumerate(hashMap):
        for lensIndex, [label, focalLength] in enumerate(lenses): 
            ans += (hashIndex + 1) * (lensIndex + 1) * focalLength
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