input_file = 'input.txt'
output_file = 'output2.txt'

# Process current scratch card 
def solve(line):
    gameId, numbers = line.split(': ')
    gameNumber = int(gameId.split(' ')[-1]) 
    winningNumbers, elfNumbers = numbers.split(' | ')
    winningNumbers = list(map(int, winningNumbers.split()))
    elfNumbers = list(map(int, elfNumbers.split()))
    
    points = 0 
    for num in elfNumbers: 
        if num in winningNumbers: 
            points += 1
    # print(points)
            
    if gameNumber > len(cardAmounts): 
        cardAmounts.append(1) 
    for i in range(gameNumber, gameNumber + points): 
        if i >= len(cardAmounts):  
            cardAmounts.append(1)
        # Add current amount to the next `points` cards  
        cardAmounts[i] += cardAmounts[gameNumber - 1]
    
# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
cardAmounts = []

for line in input: 
    solve(line.strip('\n'))
print(cardAmounts)
ans = sum(cardAmounts)
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()