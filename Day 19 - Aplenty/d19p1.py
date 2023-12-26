input_file = 'input.txt'
output_file = 'output1.txt'

class Part: 
    def __init__(self, x, m, a, s): 
        self.x = x 
        self.m = m
        self.a = a 
        self.s = s 
    
    # Applies rules from a workflow until a destination is reached
    def applyWorkflow(self, workflow): 
        for w in workflow:
            if w.lamb(self): 
                print('dest', w.dest)
                if w.dest == 'A' or w.dest == 'R': print()
                return w.dest
    
    # Returns True if the part is accepted through the workflows 
    def isAccepted(self, workflows): 
        dest = 'in'
        while dest != 'A' and dest != 'R': 
            dest = self.applyWorkflow(workflows[dest])
        return dest == 'A'

    # Returns the sum of x, m, a, s values 
    def getXmasSum(self): 
        return self.x + self.m + self.a + self.s
        
class WorkflowRule: 
    def __init__(self, lamb, dest): 
        # Lambda and destination 
        self.lamb = lamb 
        self.dest = dest

# Create and add workflow to workflows dictionary from line input  
def addWorkflow(line, workflows): 
    name, rules = line.split('{')
    rules = rules.replace('}', '').split(',')
    # print('new workflow', name, rules)

    # Convert rules list to an array of WorkflowRules 
    for ruleIndex, rule in enumerate(rules[:-1]):
        if rule.find('>') != -1: 
            rule = rule.replace(':', '>').split('>')
            lessValue = int(rule[1])
            match rule[0]:
                case 'x':
                    lamb = lambda w: w.x > lessValue
                case 'm':
                    lamb = lambda w: w.m > lessValue
                case 'a':
                    lamb = lambda w: w.a > lessValue
                case 's':
                    lamb = lambda w: w.s > lessValue
        elif rule.find('<') != -1: 
            rule = rule.replace(':', '<').split('<')
            moreValue = int(rule[1])
            match rule[0]:
                case 'x':
                    lamb = lambda w: w.x < moreValue
                case 'm':
                    lamb = lambda w: w.m < moreValue
                case 'a':
                    lamb = lambda w: w.a < moreValue
                case 's':
                    lamb = lambda w: w.s < moreValue
        dest = rule[2]
        # print('rule', lamb, '->', dest)
        rules[ruleIndex] = WorkflowRule(lamb, dest)

    # Convert last rule 
    lamb = lambda x: True 
    dest = rules[-1]
    rules[-1] = WorkflowRule(lamb, dest)

    # print('default', dest)
    # print()

    workflows[name] = rules
    return workflows

# Create and return a Part from line input  
def createPart(line):
    remove = ['{', 'x=', 'm=', 'a=', 's=', '}']
    for r in remove:
        line = line.replace(r, '')
    line = list(map(int, line.split(',')))
    part = Part(line[0], line[1], line[2], line[3])
    return part 

# Return sum of a part's xmas values if it's accepted and 0 otherwise 
def solve(line, workflows):
    print('line', line)
    part = createPart(line)
    return part.getXmasSum() if part.isAccepted(workflows) else 0 

# Open files, clear output file 
in_file = open(input_file, "r")
out_file = open(output_file, "w")
out_file.write("")

input = in_file.readlines() 
line = input.pop(0).strip('\n')
workflows = {} # workflow name -> array of lambdas 
ans = 0 

# Workflows
while line != '':
    workflows = addWorkflow(line, workflows)
    line = input.pop(0).strip('\n')

# Parts
for line in input: 
    line = line.strip('\n')
    ans += solve(line, workflows)
    
out_file.write(str(ans))

# Close files
in_file.close()
out_file.close()