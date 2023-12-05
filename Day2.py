#Day 2

#returns (id, r, g, b) denoting game id and no. of each colour ball in set
def parseBag(bagString):
    # Strip 'Game_' from string
    bagString = bagString[len("Game ") - 1:]
    ptr = 0
    # Extract Id:
    numString = ""
    while bagString[ptr] != ':':
        numString += bagString[ptr]
        ptr += 1
    id = int(numString)
    bagString = bagString[ptr+1:] # remove space after ':'
    # Split sets
    sets = [x.split(", ") for x in bagString.split("; ")]
    flattened = [x for y in sets for x in y]
    rgbCount = {"red" : 0, "green" : 0, "blue" : 0}
    for x in flattened: 
        countCol = x.split()
        rgbCount[countCol[1]] = max(rgbCount[countCol[1]], int(countCol[0]))
    return (id, tuple(rgbCount.values()))

def partOne():
    file = open("Day_2_input.txt", "r")
    total = 0
    for line in file.readlines():
        print((line))
        (id, (r, g, b)) = parseBag(line)
        if r <= 12 and g <= 13 and b <= 14:
            total += id
    file.close()
    return total

def partTwo():
    file = open("Day_2_input.txt", "r")
    total = 0
    for line in file.readlines():
        (id, (r, g, b)) = parseBag(line)
        total += r * g * b
    file.close()
    return total

def test():
    file = open("Day_2_input.txt", "r")
    for c in file:
        print(c)
        


# print(partOne())
# print(partTwo())
test()
