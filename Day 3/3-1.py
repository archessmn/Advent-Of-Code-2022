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

for l in range(len(lines)):
    part1 = lines[l][:(int(len(lines[l])/2))]
    part2 = lines[l][(int(len(lines[l])/2)):]

    for c in range(len(part1)):
        if part1[c] in part2:
            total += getWeight(part1[c])
            break


print(total)