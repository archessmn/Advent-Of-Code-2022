import os
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

# testing = True

with open(f"{cwd}/Day 7/7-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

path = []
directories = []

for l in range(len(lines)):
    line = lines[l]
    if line[0:4] == "$ cd":
        if line[5:-1] == "..":
            path.pop(-1)
        else:
            path.append(line[5:-1])
            directories.append(["/".join(path), [], 0, 0])
    elif line[0:3] == "dir":
        for d in range(len(directories)):
            directory = directories[d]
            if directory[0] == "/".join(path):
                directories[d][1].append(f"{'/'.join(path)}/{line[4:-1]}")
                break
    elif line[0:4] == "$ ls":
        continue
    else:
        parts = line.split(" ")
        fileSize = int(parts[0])
        for d in range(len(directories)):
            directory = directories[d]
            if directory[0] == "/".join(path):
                directories[d][2] += fileSize
                break


def calculateDirSize(dir):
    for d in range(len(directories)):
        directory = directories[d]
        if directory[0] == dir:
            # print("Dir found")
            for i in range(len(directories[d][1])):
                directories[d][3] += calculateDirSize(directories[d][1][i])
            directories[d][3] += directories[d][2]
            return directories[d][3]

for d in range(len(directories)):
    directory = directories[d]
    if len(directory[1]) == 0:
        directories[d][3] = directories[d][2]

def betterCalcDirSize(dir):
    for d in range(len(directories)):
        directory = directories[d]
        if directory[0] == dir:
            if len(directory[1]) == 0:
                directories[d][3] = directories[d][2]
                return directories[d][3]
            else:
                for i in range(len(directories[d][1])):
                    print(f"Calling calculation on dir {directories[d][1][i]}")
                    directories[d][3] += betterCalcDirSize(directories[d][1][i])
                directories[d][3] += directories[d][2]
                return directories[d][3]
            break

    return

# calculateDirSize(path[0])


for o in range(len(directories)):
    oName = directories[o][0]
    for i in range(len(directories[o][1])):
        for u in range(len(directories)):
            if directories[u][0] == directories[o][1][i]:
                if len(directories[u][1]) == 0:
                    continue
                elif oName in directories[u][1]:
                    print("Well fuck")


betterCalcDirSize(path[0])




totalLess = 0

otherTotal = 0

for d in range(len(directories)):
    directory = directories[d]
    if directory[3] <= 100000:
        totalLess += 1
        otherTotal += directory[3]

print(totalLess)
print(otherTotal)

# print(directories)


totalFS = 70000000
freeSpace = totalFS - directories[0][3]
spaceNeeded = 30000000 - freeSpace

smallestDirectory = totalFS

for d in range(len(directories)):
    directory = directories[d]
    if spaceNeeded <= directory[3] <= smallestDirectory:
        smallestDirectory = directory[3]

print(smallestDirectory)