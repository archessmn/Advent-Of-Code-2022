import os
import copy
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

# testing = True

with open(f"{cwd}/Day 12/12-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

grid = []


def printGrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            print(f"{'[' if grid[x][y][1] else ' '}{grid[x][y][0]}{']' if grid[x][y][1] else ' '}", end="")
        print("")

startPointer = []
endPointer = []

start = []
end = []

for x in range(len(lines[0].replace("\n", ""))):
    grid.append([])
    for y in range(len(lines)):
        line = lines[y].replace("\n", "")
        if line[x] == "S":
            start = [x, y]
        if line[x] == "E":
            end = [x, y]
        grid[x].append([line[x], 0])

nodes = []

for x in range(len(lines[0].replace("\n", ""))):
    for y in range(len(lines)):
        line = lines[y].replace("\n", "")
        nodes.append([line[x], [x,y], (int(len(lines) * len(line) + 1)), False, -1, []])
        
        grid[x][y][1] = len(nodes) - 1

        if line[x] == "S":
            nodes[-1][2] = 0
            startPointer = len(nodes) - 1
        if line[x] == "E":
            endPointer = len(nodes) - 1


for n in range(len(nodes)):
    node = nodes[n]
    for o in range(-1, 2):
        oCoord = node[1][0] + o
        if 0 <= oCoord <= len(grid) - 1:
            for i in range(-1, 2):
                iCoord = node[1][1] + i
                if 0 <= iCoord <= len(grid[0]) - 1:
                    if abs(o) != abs(i):
                        
                        inspectingCoords = [oCoord, iCoord]
                        inspectingGrid = grid[oCoord][iCoord]

                        if node[0] == "S" or inspectingGrid[0] == "E":
                            if (node[0] == "S" and inspectingGrid[0] == "a") or (node[0] == "z" and inspectingGrid[0] == "E"):
                                nodes[n][5].append(inspectingGrid[1])
                        elif ((ord(node[0]) - ord(inspectingGrid[0])) >= -1):
                            nodes[n][5].append(inspectingGrid[1])

                        # print(grid[oCoord][iCoord])

for n in range(len(nodes)):
    shortestPathToStart = (int(len(lines) * len(line) + 1))
    shortestPointer = 0
    for i in range(len(nodes)):
        if (nodes[i][2] < shortestPathToStart) and (not nodes[i][3]):
            shortestPathToStart = nodes[i][2]
            shortestPointer = i
    
    for i in range(len(nodes[shortestPointer][5])):
        inspectedChildNode = nodes[nodes[shortestPointer][5][i]]
        if not inspectedChildNode[3]:
            if nodes[shortestPointer][2] + 1 < inspectedChildNode[2]:
                nodes[nodes[shortestPointer][5][i]][2] = nodes[shortestPointer][2] + 1
                nodes[nodes[shortestPointer][5][i]][4] = shortestPointer
    
    nodes[shortestPointer][3] = True

# print(nodes[3177])
for y in range(len(grid[0])):
    for x in range(len(grid)):
        isSolved = True if nodes[grid[x][y][1]][2] != (int(len(lines) * len(line) + 1)) else False
        print(f"{'[' if isSolved else ' '}{grid[x][y][0]}{'' if isSolved else ''}", end="")
    print("")

print(nodes[endPointer][2])

node = nodes[endPointer]

for i in range(nodes[endPointer][2]):
    print(node[0])
    node = nodes[node[4]]












# for l in range(len(lines)):
#     line = lines[l].replace("\n", "")
#     grid.append([])
#     for y in range(len(line)):
#         if line[y] == "S":
#             start = [l, y]
#         if line[y] == "E":
#             end = [l, y]
#         grid[l].append([line[y], False, -1, [], []])

# print(start)

# grid[start[0]][start[1]][2] = 0

# x = start[0]
# y = start[1]

# lowestCoords = copy.deepcopy(start)

# currentCoords = copy.deepcopy(start)
# currentGrid = grid[x][y]












# while True:
#     for o in range(-1, 2):
#         oCoord = lowestCoords[0] + o
#         if 0 <= oCoord <= len(grid) - 1:
#             for i in range(-1, 2):
#                 iCoord = lowestCoords[1] + i
#                 if 0 <= iCoord <= len(grid[0]) - 1:
#                     if o != i:
#                         checking = grid[oCoord][iCoord]
#                         if (checking[0] == "E" and currentGrid[0] == "z") or (not checking[1]) and ((currentCoords == start and checking[0] == "a") or ord(checking[0]) == ord(currentGrid[0]) or ord(checking[0]) == ord(currentGrid[0]) + 1):
#                             if 0 <= grid[lowestCoords[0]][lowestCoords[1]][2] + 1 < checking[2] or checking[2] == -1:
#                                 grid[oCoord][iCoord][3] = [lowestCoords[0], lowestCoords[1]]
#                                 grid[oCoord][iCoord][2] = grid[lowestCoords[0]][lowestCoords[1]][2] + 1

#     lowestCoords = []
#     shortestFromStart = -2
#     for o in range(len(grid)):
#         for i in range(len(grid[0])):
#             currentCoords = [o,i]
#             currentGrid = grid[o][i]
#             if (currentGrid[2] == -1 and shortestFromStart == -2) or (currentGrid[2] < shortestFromStart) or (currentGrid[2] < shortestFromStart):
#                 lowestCoords = currentCoords
#                 shortestFromStart = currentGrid[2]
#     currentCoords = [lowestCoords[0],lowestCoords[1]]
#     currentGrid = grid[lowestCoords[0]][lowestCoords[1]]
    


#     grid[x][y][1] = True

#     allVisited = True

#     for o in range(-1, 2):
#         oCoord = end[0] + o
#         if 0 <= oCoord <= len(grid) - 1:
#             for i in range(-1, 2):
#                 iCoord = end[1] + i
#                 if 0 <= iCoord <= len(grid[0]) - 1:
#                     if o != i:
#                         if grid
    
#     if allVisited:
#         break

# print(grid[lowestCoords[0]][lowestCoords[1]])


            



# # for x in range(len(grid)):
# #     for y in range(len(grid[0])):
# #         currentCoords = [x,y]
# #         currentGrid = grid[x][y]
# #         for o in range(-1, 2):
# #             oCoord = x + o
# #             if 0 <= oCoord <= len(grid) - 1:
# #                 for i in range(-1, 2):
# #                     iCoord = y + i
# #                     if 0 <= iCoord <= len(grid[0]) - 1:
# #                         if o != i:
# #                             checking = grid[oCoord][iCoord]
# #                             if (not checking[1]) and ((currentCoords == start and checking[0] == "a") or ord(checking[0]) == ord(currentGrid[0]) or ord(checking[0]) == ord(currentGrid[0]) + 1):
# #                                 if 0 <= grid[x][y][2] + 1 < checking[2] or checking[2] == -1:
# #                                     grid[oCoord][iCoord][3] = [x, y]
# #                                     grid[oCoord][iCoord][2] = grid[x][y][2] + 1

# #         grid[x][y][1] = True

# # print(grid)

# for x in range(len(grid)):
#         for y in range(len(grid[0])):
#             print(f"{grid[x][y]}", end="")
#         print("")

# printGrid(grid)
