# Day 14
from collections import defaultdict
def partOne():
    file = open("Day_14_input.txt", "r")
    lineLength = len(file.readline().strip())
    file.seek(0,0) # resets the pointer to the beginning
    northRowMax = [0] * lineLength
    roundRocks = defaultdict(int)
    lineCount = 0
    for line in file.readlines():
        print(northRowMax)
        print(roundRocks)
        lineCount += 1
        chars = line.strip()
        print(chars)
        for i in range(lineLength):
            if chars[i] == 'O':
                roundRocks[northRowMax[i] + 1] += 1
                northRowMax[i] += 1
                continue
            if chars[i] == '#':
                northRowMax[i] = lineCount
    print(roundRocks)
    
    total = 0
    for r, c in roundRocks.items():
        total += (lineCount - r + 1) * c 
    file.close()
    return total 

print(partOne())


        