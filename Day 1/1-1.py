with open('c:/Users/maxmo/Personal/Code/Advent Of Code/Day 1/1-1_input.txt', "r") as f:
    lines = f.readlines()

calories = 0
highest = [0,0,0]

for i in range(len(lines)):
    line = lines[i].replace("\n", "")

    if line == "":
        for o in range(3):
            if calories > highest[o]:
                temp = highest[o]
                highest[o] = calories
                calories = temp
        # if calories > highest:
        #     highest = calories
        # print(calories)
        calories = 0
    else:
        calories += int(line)
    # print(line)
print(len(lines))

print(highest)

total = 0

for i in range(3):
    total += highest[i]

print(total)