import os
cwd = os.getcwd().replace("\\", "/")

testing = False

# Uncomment line below to use input file ending with _testing.txt

# testing = True

with open(f"{cwd}/Day 10/10-1_input{'_testing' if testing else ''}.txt") as f:
    lines = f.readlines()


cycle = 0

register = 1

counter = 0

toAdd = 0

add = False

signalStrength = 0

while counter < len(lines):
    line = lines[counter].replace("\n", "")
    cycle += 1

    if cycle % 40 == 20:
        signalStrength += cycle * register

    if add:
        register += toAdd
        add = False
        counter += 1
    else:
        if line[:4] == "noop":
            counter += 1
        else:
            toAdd = int(line[4:])
            add = True

print(signalStrength)