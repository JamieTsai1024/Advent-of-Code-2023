from collections import defaultdict

input_file = 'input.txt'
output_file = 'output2.txt'

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
    order = 'J23456789TQKA'
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
# Values: promotions array (max promotions with <index>+1 Js), cards of that type
types = {
    'high card': [[1], []],                     # 1 -> 1 (one pair), can't have more Js in this type 
    'one pair': [[2, 2], []],                   # 1 -> 2 (three of a kind), 2 -> 2 (three of a kind; even though two pair can be formed, it's not the max promotion), can't have more Js in this type 
    'two pair': [[2, 3], []],                   # 1 -> 2 (full house), 2 -> 3 (four of a kind), can't have more Js in this type 
    'three of a kind': [[2, 0, 2], []],         # 1 -> 2 (four of a kind), 2 -> - (impossible since we have a set of 3, 1, 1), 3 -> 2 (four of a kind), can't have more Js in this type 
    'full house': [[0, 2, 2], []],              # 1 -> - (impossible since we have a set of 2 and 3), 2 -> 2 (five of a kind), 3 -> 2 (five of a kind), can't have more Js in this type 
    'four of a kind': [[1, 0, 0, 1], []],       # 1 -> 1 (five of a kind), 2 & 3 -> - (impossible since we have a set of 1 and 4), 4 -> 1 (five of a kind), can't have more Js in this type 
    'five of a kind': [[0, 0, 0, 0, 0], []],    # No promotions possible 
}

for line in input: 
    card, bid = line.strip('\n').split(' ') 
    bid = int(bid)
    types[getType(card)][1].append([card, bid])

# print("before", types)

# Promote cards with J
for typeIndex, type in reversed(list(enumerate(types))): # Promote higher cards first to avoid promoting a card multiple times
    promotions = types[type][0]
    # print('type', typeIndex, type)
    for i, hand in reversed(list(enumerate(types[type][1]))):
        card, bid = hand
        # print('card', card)
        j = card.count('J')
        if j != 0: 
            # Move (add and delete) promoted hand to proper location  
            promotionDelta = promotions[j - 1]
            promotionLocation = list(types.keys())[typeIndex + promotionDelta]
            print('promotion', card, promotionDelta, '-', type, 'to', promotionLocation)
            types[promotionLocation][1].append([card, bid])
            del types[type][1][i] 

# print("after", types)
bids = [] 
for type in types: 
    types[type][1].sort(key=customSort) 
    for card, bid in types[type][1]: 
        # print(card)
        bids.append(bid)

# print(bids)
for i, bid in enumerate(bids): 
    ans += (i + 1) * bid 

out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()