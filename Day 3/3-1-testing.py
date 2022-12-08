def getWeight(char):
    if ord(char) > 96:
        return ord(char) - 96
    else:
        return ord(char) - 38

print(getWeight("Z"))