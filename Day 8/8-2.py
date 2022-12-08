import os
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

# testing = True

with open(f"{cwd}/Day 8/8-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

width = len(lines[0].replace("\n", ""))

height = len(lines)

# print(width)
# print(height)

visible = int(((width - 1) * 2) + ((height - 1) * 2))

greatestDistance = 0

for h in range(1, height - 1):
    for w in range(1, width - 1):
        tree = int(lines[h][w])
        # Check vertically

        vUp = 1
        vDown = 1
        vLeft = 1
        vRight = 1

        for x in range(1, w):
            compTree = int(lines[h][w - x])
            if compTree >= tree:
                break
            else:
                vLeft += 1
        
        for x in range(w + 1, width - 1):
            compTree = int(lines[h][x])
            if compTree >= tree:
                break
            else:
                vRight += 1
        
        for y in range(1, h):
            compTree = int(lines[h - y][w])
            if compTree >= tree:
                break
            else:
                vUp += 1
        
        for y in range(h + 1, height - 1):
            compTree = int(lines[y][w])
            if compTree >= tree:
                break
            else:
                vDown += 1

        scenicScore = vUp * vDown * vLeft * vRight

        if scenicScore > greatestDistance:
            greatestDistance = scenicScore

print(greatestDistance)
