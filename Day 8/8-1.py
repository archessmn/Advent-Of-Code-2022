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

for h in range(1, height - 1):
    for w in range(1, width - 1):
        tree = int(lines[h][w])
        # Check vertically

        isVisible = False

        flagVisible1 = True
        flagVisible2 = True

        for y in range(height):
            if y < h:
                if int(lines[y][w]) >= tree:
                    flagVisible1 = False
            elif y > h:
                if int(lines[y][w]) >= tree:
                    flagVisible2 = False
        
        if flagVisible1 or flagVisible2:
            isVisible = True
        
        # Check horizontally

        flagVisible1 = True
        flagVisible2 = True

        for x in range(width):
            if x < w:
                if int(lines[h][x]) >= tree:
                    flagVisible1 = False
            elif x > w:
                if int(lines[h][x]) >= tree:
                    flagVisible2 = False
        
        if flagVisible1 or flagVisible2:
            isVisible = True

        if isVisible:
            visible += 1

print(visible)
