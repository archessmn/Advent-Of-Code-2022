import os
import copy
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

testing = True

with open(f"{cwd}/Day 12/12-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

grid = []


def printGrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            print(f"{'[' if grid[x][y][1] else ' '}{grid[x][y][0]}{']' if grid[x][y][1] else ' '}", end="")
        print("")

start = []
end = []

for l in range(len(lines)):
    line = lines[l].replace("\n", "")
    grid.append([])
    for y in range(len(line)):
        if line[y] == "S":
            start = [l, y]
        if line[y] == "E":
            end = [l, y]
        grid[l].append([line[y], False, -1, []])

print(start)

grid[start[0]][start[1]][2] = 0

x = start[0]
y = start[1]

lowestCoords = copy.deepcopy(start)

currentCoords = copy.deepcopy(start)
currentGrid = grid[x][y]

while True:
    for o in range(-1, 2):
        oCoord = lowestCoords[0] + o
        if 0 <= oCoord <= len(grid) - 1:
            for i in range(-1, 2):
                iCoord = lowestCoords[1] + i
                if 0 <= iCoord <= len(grid[0]) - 1:
                    if o != i:
                        checking = grid[oCoord][iCoord]
                        if (checking[0] == "E" and currentGrid[0] == "z") or (not checking[1]) and ((currentCoords == start and checking[0] == "a") or ord(checking[0]) == ord(currentGrid[0]) or ord(checking[0]) == ord(currentGrid[0]) + 1):
                            if 0 <= grid[lowestCoords[0]][lowestCoords[1]][2] + 1 < checking[2] or checking[2] == -1:
                                grid[oCoord][iCoord][3] = [lowestCoords[0], lowestCoords[1]]
                                grid[oCoord][iCoord][2] = grid[lowestCoords[0]][lowestCoords[1]][2] + 1

    lowestCoords = []
    shortestFromStart = -2
    for o in range(len(grid)):
        for i in range(len(grid[0])):
            currentCoords = [o,i]
            currentGrid = grid[o][i]
            if (currentGrid[2] == -1 and shortestFromStart == -2) or (currentGrid[2] < shortestFromStart) or (currentGrid[2] < shortestFromStart):
                lowestCoords = currentCoords
                shortestFromStart = currentGrid[2]
    currentCoords = [lowestCoords[0],lowestCoords[1]]
    currentGrid = grid[lowestCoords[0]][lowestCoords[1]]
    


    grid[x][y][1] = True

    allVisited = True

    for o in range(-1, 2):
        oCoord = end[0] + o
        if 0 <= oCoord <= len(grid) - 1:
            for i in range(-1, 2):
                iCoord = end[1] + i
                if 0 <= iCoord <= len(grid[0]) - 1:
                    if o != i:
                        if grid
    
    if allVisited:
        break

print(grid[lowestCoords[0]][lowestCoords[1]])


            



# for x in range(len(grid)):
#     for y in range(len(grid[0])):
#         currentCoords = [x,y]
#         currentGrid = grid[x][y]
#         for o in range(-1, 2):
#             oCoord = x + o
#             if 0 <= oCoord <= len(grid) - 1:
#                 for i in range(-1, 2):
#                     iCoord = y + i
#                     if 0 <= iCoord <= len(grid[0]) - 1:
#                         if o != i:
#                             checking = grid[oCoord][iCoord]
#                             if (not checking[1]) and ((currentCoords == start and checking[0] == "a") or ord(checking[0]) == ord(currentGrid[0]) or ord(checking[0]) == ord(currentGrid[0]) + 1):
#                                 if 0 <= grid[x][y][2] + 1 < checking[2] or checking[2] == -1:
#                                     grid[oCoord][iCoord][3] = [x, y]
#                                     grid[oCoord][iCoord][2] = grid[x][y][2] + 1

#         grid[x][y][1] = True

# print(grid)

for x in range(len(grid)):
        for y in range(len(grid[0])):
            print(f"{grid[x][y]}", end="")
        print("")

printGrid(grid)
