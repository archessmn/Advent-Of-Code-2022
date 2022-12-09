import os
import copy
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

# testing = True

with open(f"{cwd}/Day 9/9-{'2' if testing else '1'}_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()


# Calculate grid space
coords = [0,0]

coordsMinMax = [[0,0],[0,0]]

for l in range(len(lines)):
    direction = lines[l][0]
    moves = int(lines[l][2:].replace("\n", ""))
    match direction:
        case "R":
            coords[0] += moves
        case "L":
            coords[0] -= moves
        case "U":
            coords[1] += moves
        case "D":
            coords[1] -= moves
    # print(coords)
    if coords[0] < coordsMinMax[0][0]:
        coordsMinMax[0][0] = coords[0]
    elif coords[0] > coordsMinMax[1][0]:
        coordsMinMax[1][0] = coords[0]
    if coords[1] < coordsMinMax[0][1]:
        coordsMinMax[0][1] = coords[1]
    elif coords[1] > coordsMinMax[1][1]:
        coordsMinMax[1][1] = coords[1]

print(coordsMinMax)

grid = []

startCoords = [0 - coordsMinMax[0][0], 0 - coordsMinMax[0][1]]
print(startCoords)

knotCoords = []

for i in range(10):
    knotCoords.append(copy.deepcopy(startCoords))


# headCoords = [0 - coordsMinMax[0][0], 0 - coordsMinMax[0][1]]
# knotCoords[x+1] = [0 - coordsMinMax[0][0], 0 - coordsMinMax[0][1]]


for x in range(coordsMinMax[1][0] - coordsMinMax[0][0] + 1):
    grid.append([])
    for y in range(coordsMinMax[1][1] - coordsMinMax[0][1] + 1):
        grid[x].append([0])


for l in range(len(lines)):
    direction = lines[l][0]
    moves = int(lines[l][2:].replace("\n", ""))
    for m in range(moves):
        match direction:
            case "R":
                knotCoords[0][0] += 1
            case "L":
                knotCoords[0][0] -= 1
            case "U":
                knotCoords[0][1] += 1
            case "D":
                knotCoords[0][1] -= 1
        
        for x in range(len(knotCoords) - 1):


            xDif = knotCoords[x][0] - knotCoords[x+1][0]
            yDif = knotCoords[x][1] - knotCoords[x+1][1]

            # print("")
            # print(xDif)
            # print(yDif)

            if not -1 <= xDif <= 1:
                # print(xDif)
                # print(f"Moving x by {int(xDif / 2)}")
                knotCoords[x+1][0] += (1 if xDif > 0 else -1)
                if not yDif == 0:
                    knotCoords[x+1][1] += (1 if yDif > 0 else -1)
            elif not -1 <= yDif <= 1:
                # print(yDif)
                # print(f"Moving y by {int(yDif / 2)}")
                knotCoords[x+1][1] += (1 if yDif > 0 else -1)
                if not xDif == 0:
                    knotCoords[x+1][0] += (1 if xDif > 0 else -1)
        grid[knotCoords[9][0]][knotCoords[9][1]][0] += 1

    


        # print(knotCoords[x])
        # print(knotCoords[x+1])

count = 0

for y in range(len(grid[0])):
    print("")
    for x in range(len(grid)):

        aY = len(grid[0]) - y - 1

        if [x,aY] == startCoords:
            print("S", end="")
        elif grid[x][aY][0] >= 1:
            print("#", end="")
        else:
            print(".", end="")

        if grid[x][aY][0] >= 1:
            count += 1

print("")
print(count)