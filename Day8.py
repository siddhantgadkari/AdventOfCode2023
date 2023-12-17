# Day 8
from math import gcd
from functools import reduce
def partOne():
    f = open("Day_8_input.txt", "r")

    instructions = f.readline()[:-1]

    instructions = [0 if i == 'L' else 1 for i in instructions]
    network = {}
    for line in f.readlines()[1:]:
        network[line[:3]] = (line[7:10], line[12:15])

    # print(type((list(network.keys())[0])))

    curr = "AAA"
    steps = 0
    iPtr = 0
    while curr != "ZZZ":
        if iPtr == len(instructions):
            iPtr = 0
        
        curr = network[curr][instructions[iPtr]]
        iPtr += 1
        steps += 1

    f.close()
    return steps

def partTwo():
    f = open("Day_8_input.txt", "r")

    instructions = f.readline()[:-1]
    print(instructions)
    start = []
    instructions = [0 if i == 'L' else 1 for i in instructions]
    network = {}
    for line in f.readlines()[1:]:
        key = line[:3]
        if key[2] == 'A':
            start.append(key)
        network[key] = (line[7:10], line[12:15])
    # print(network)
    # print(type((list(network.keys())[0])))
    # print(instructions)
    steps = []
    print(start)
    for each in start:
        curr = each
        s = 0
        iPtr = 0
        while not curr[2] == 'Z':
            if iPtr == len(instructions):
                iPtr = 0
            
            curr = network[curr][instructions[iPtr]] 
            iPtr += 1
            s += 1
        steps.append(s)

    f.close()
    def lcm(nums):
        return reduce(lambda x, y: x*y // gcd(x,y), nums)
    return lcm(steps)

print(partTwo())