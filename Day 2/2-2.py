with open('c:/Users/maxmo/Personal/Code/Advent Of Code/Day 2/2-1_input.txt', "r") as f:
    lines = f.readlines()

# Win =      6
# Draw =     3
# Loss =     0
#
# Rock =     1  A X
# Paper =    2  B Y
# Scissors = 3  C Z

def calculatePoints(line):
    totalPoints = 0
    gamePoints = 0
    choices = line.split(" ")
    choicePoints = ord(choices[1]) - 87
    elfPoints = ord(choices[0]) - 64

    if choicePoints == elfPoints:
        gamePoints = 3
    elif choicePoints == (elfPoints + 1) % 3 or choicePoints == (elfPoints + 1):
        gamePoints = 6
    else:
        gamePoints = 0
    
    totalPoints = gamePoints + choicePoints

    return totalPoints

def pickChoice(line):
    choiceGame = line.split(" ")
    choicePoints = 0
    elfChoice = ord(choiceGame[0]) - 64
    match choiceGame[1]:
        case "X":
            choicePoints = 3 if elfChoice == 1 else elfChoice - 1
        case "Y":
            choicePoints = elfChoice
        case "Z":
            choicePoints = 1 if elfChoice == 3 else elfChoice + 1
    return choicePoints

def calcGamePoints(line):
    gamePoints = 0
    choiceGame = line.split(" ")
    gamePoints = (ord(choiceGame[1]) - 88) * 3
    return gamePoints

total = 0

for i in range(len(lines)):
    line = lines[i].replace("\n", "")
    total += (calcGamePoints(line) + pickChoice(line))
    print(f"{line}  {calcGamePoints(line) + pickChoice(line)}")

print(f"Total:  {total}")