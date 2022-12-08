import os
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

testing = True

with open(f"{cwd}/Day 6/6-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()

buffer = []

for c in range(len(lines[0])):
    char = lines[0][c]
    if len(buffer) == 14:
        buffer.pop(13)
    buffer.insert(0, char)
    if len(buffer) == 14:
        repeated = False
        for o in range(14):
            for i in range(14):
                if o != i and buffer[o] == buffer[i]:
                    repeated = True
        if not repeated:
            print(c + 1)
            break

print(buffer)