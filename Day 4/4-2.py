import os
cwd = os.getcwd().replace("\\", "/")

testing = False
# testing = True

with open(f"{cwd}/Day 4/4-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

totalOverlapping = 0

for l in range(len(lines)):
    line = lines[l]
    pairs = line.split(",")
    bounds = [pairs[0].split("-"), pairs[1].split("-")]

    for o in range(2):
        for i in range(2):
            bounds[o][i] = int(bounds[o][i])

    if (bounds[0][0] <= bounds[1][0] <= bounds[0][1]) or (bounds[1][0] <= bounds[0][0] <= bounds[1][1]):
        totalOverlapping += 1

print(totalOverlapping)