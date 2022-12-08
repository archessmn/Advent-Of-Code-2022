import os
cwd = os.getcwd().replace("\\", "/")

testing = False
# testing = True

with open(f"{cwd}/Day 5/5-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

height = 0

stacks = []

for l in range(len(lines)):
    line = lines[l]
    if line[1] != "1":
        height += 1
    else:
        widthTemp = line.replace("   ", " ").replace("\n", "").split(" ")
        # for 
        width = int(widthTemp[-2])
        break

print(height)
print(width)

for o in range(width):
    stacks.append([])

for h in range(height):
    hInv = height - h - 1
    line = lines[hInv]
    for c in range(width):
        cStart = c * 4
        cEnd = (c * 4) + 3
        column = line[cStart:cEnd]

        if column != "   ":
            stacks[c].append(column[1])

            print(stacks[c][h], end=" ")
        else:
            print(" ", end=" ")
    print("")

def printStacks(stacks):
    width = len(stacks)

    height = 0

    for c in range(len(stacks)):
        if len(stacks[c]) > height:
            height = len(stacks[c])

    print(height)

    for h in range(height):
        hInv = height - h - 1
        for w in range(width):
            try:
                print(stacks[w][hInv], end=" ")
            except:
                print(" ", end=" ")
        print("")

printStacks(stacks)

instructions = []

for i in range(height + 2, len(lines)):
    line = lines[i]
    for r in [["move ", ""], [" from ", " "], [" to ", " "], ["\n", ""]]:
        line = line.replace(r[0], r[1])
    instructions.append(line.split(" "))

for o in range(len(instructions)):
    for i in range(3):
        instructions[o][i] = int(instructions[o][i])

for i in range(len(instructions)):
    cir = instructions[i]
    # print(cir)
    for c in range(int(cir[0])):
        toMove = stacks[cir[1] - 1][-1]
        stacks[cir[1] - 1].pop(-1)
        stacks[cir[2] - 1].append(toMove)
    printStacks(stacks)



for c in range(len(stacks)):
    try:
        print(stacks[c][-1], end = "")
    except:
        print(" ", end = "")