# Day 4
from collections import defaultdict

def partOne():
    file = open("Day_4_input.txt", "r")
    total = 0
    for line in file.readlines():
        while line[0] != ':':
            line = line[1:]
        line = line[1:].split(' | ')
        player = [int(x) for x in line[0].split()]
        card =   [int(x) for x in line[1].split()]

        matches = 0
        for i in player: 
            if i in card:
                matches += 1
        if matches > 0:
            total += 2 ** (matches - 1)
    return total

def partTwo():
    file = open("Day_4_input.txt", "r")
    matchCount = defaultdict(int)
    lineCount = 1
    for line in file.readlines():
        while line[0] != ':':
            line = line[1:]
        line = line[1:].split(' | ')
        player = [int(x) for x in line[0].split()]
        card =   [int(x) for x in line[1].split()]

        matches = 0
        for i in player: 
            if i in card:
                matches += 1
        matchCount[lineCount] = matches
        lineCount += 1
    
    copyCount = {i: 1 for i in range(1, len(matchCount) + 1)}
    for game, m in matchCount.items():
        for i in range(1, m + 1):
            copyCount[game + i] += copyCount[game]
    return sum(copyCount.values())



print(partTwo())
