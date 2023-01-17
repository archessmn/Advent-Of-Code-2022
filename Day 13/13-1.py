import os
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

testing = True

with open(f"{cwd}/Day 13/13-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

pairs = []

def comparePairs(partOne, partTwo):

    shortest = 0 if len(partOne) <= len(partTwo) else 1

    remaining = [len(partOne), len(partTwo)]

    while len(partOne) != 0 and len(partTwo) != 0:
        if isinstance(partOne[0], int) and isinstance(partOne[0], int):
            if partOne[0] > partTwo[0]:
                return False



        del partOne[0]
        del partTwo[0]

    shortest = 0 if len(partOne) <= len(partTwo) else 1

    for i in range(len(partOne) if shortest == 0 else len(partTwo)):
        print(i)
    print("")




for l in range(int((len(lines) + 1)/3)):
    pairs.append([])
    for i in range(2):
        pairs[l].append(eval(lines[(l * 3) + i].replace("\n", "")))
    
    comparePairs(l)



        

print(pairs)


