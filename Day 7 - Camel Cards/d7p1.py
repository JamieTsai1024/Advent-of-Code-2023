from collections import defaultdict

input_file = 'input.txt'
output_file = 'output1.txt'

# Return whether the game is possible (id value) or impossible (0)
def getType(card):
    labels = defaultdict(int)
    for c in card: 
        labels[c] += 1

    if 5 in labels.values():
        return 'five of a kind'
    elif 4 in labels.values(): 
        return 'four of a kind'
    elif 3 in labels.values() and 2 in labels.values(): 
        return 'full house'
    elif 3 in labels.values(): 
        return 'three of a kind'
    elif list(labels.values()).count(2) == 2: 
        return 'two pair'
    elif 2 in labels.values(): 
        return 'one pair'
    return 'high card'

# Hash the hand value so that each hand is unique and can be ranked 
def customSort(t):
    order = '23456789TJQKA'
    t = t[0]
    orderHash = 0
    for i in range(len(t)):
        orderHash += order.find(t[i]) + 1
        orderHash *= 13
    return orderHash

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
ans = 0 
types = {
    'high card': [],
    'one pair': [], 
    'two pair': [], 
    'three of a kind': [], 
    'full house': [], 
    'four of a kind': [], 
    'five of a kind': [], 
}

for line in input: 
    card, bid = line.strip('\n').split(' ') 
    bid = int(bid)
    types[getType(card)].append([card, bid])

bids = [] 
for type in types: 
    types[type].sort(key=customSort) 
    for card, bid in types[type]: 
        bids.append(bid)

for i, bid in enumerate(bids): 
    ans += (i + 1) * bid 

out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()