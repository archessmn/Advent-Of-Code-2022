import os
cwd = os.getcwd().replace("\\", "/")

with open(f"{cwd}/Day 3/3-1_input.txt") as f:
    lines = f.readlines()


def getWeight(char):
    if ord(char) > 96:
        return ord(char) - 96
    else:
        return ord(char) - 38

total = 0

for l in range(int(len(lines)/3)):
    # part1 = lines[l][:(int(len(lines[l])/2))]
    # part2 = lines[l][(int(len(lines[l])/2)):]
    bag = [lines[l*3], lines[l*3 + 1], lines[l*3 + 2]]

    for c in range(len(bag[0])):
        if bag[0][c] in bag[1] and bag[0][c] in bag[2]:
            print(bag[0][c])
            total += getWeight(bag[0][c])
            break


print(total)