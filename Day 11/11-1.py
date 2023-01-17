import os
import math
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

# testing = True

with open(f"{cwd}/Day 11/11-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

currentMonkey = 0

numMonkeys = int(lines[-6].replace("\n", "")[7:-1]) + 1

# print(numMonkeys)

monkeys = []

for m in range(numMonkeys):
    currentMonkey = m
    lineOffset = m * 7
    startingItems = lines[lineOffset + 1].replace("\n", "")[18:].split(", ")
    operation = lines[lineOffset + 2].replace("\n", "")[13:]
    testNum = int(lines[lineOffset + 3].replace("\n", "")[21:])
    ifTrue = int(lines[lineOffset + 4].replace("\n", "")[29:])
    ifFalse = int(lines[lineOffset + 5].replace("\n", "")[30:])

    monkeys.append([startingItems, operation, testNum, ifTrue, ifFalse, 0])

# for m in range(len(monkeys)):
#     print(monkeys[m])

for r in range(20):
    for m in range(numMonkeys):
        monkey = monkeys[m]
        for i in range(len(monkey[0])):
            monkeys[m][5] += 1
            old = int(monkey[0][i])
            new = 0
            exec(monkey[1])
            new = math.floor(new / 3)
            if new % monkey[2] == 0:
                monkeys[monkey[3]][0].append(new)
            else:
                monkeys[monkey[4]][0].append(new)
        monkeys[m][0].clear()

highest = [0,0]

for m in range(numMonkeys):
    inspected = monkeys[m][5]
    for i in range(2):
        if inspected > highest[i]:
            highest.insert(i, inspected)
            del highest[2]
            break

# print(highest)

print(highest[0] * highest[1])