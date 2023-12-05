#Day 3
""" 
I'm sorry to whoever has to read this code..
(probably just me again: hi future me.. err what can I tell you that's nostalic.. err.. your wrist was bugging) 

"""

def getRegion(coords):
    regionSet = set()
    for i in range(0, len(coords)):
        (r, c) = coords[i]
        regionSet.add((r-1,c))
        regionSet.add((r+1,c))
        if i == 0:
            regionSet.add((r-1,c-1))
            regionSet.add((r,c-1))
            regionSet.add((r+1, c-1))
        if i == len(coords) - 1:
            regionSet.add((r-1,c+1))
            regionSet.add((r,c+1))
            regionSet.add((r+1,c+1))
    return regionSet

def partOne():
    file = open("Day_3_input.txt", "r").read()
    nums, symbols = [], []
    rowPtr, colPtr = 0, 0 
    parseNumFlag = False
    numString, numStringCoords = "", []


    for c in file: 
        if parseNumFlag:
            if c.isdigit():
                numString += c
                numStringCoords.append((rowPtr, colPtr))
                colPtr += 1
                continue
            else:
                parseNumFlag = False
                nums.append((int(numString), getRegion(numStringCoords)))
                numString = ""
                numStringCoords = []
                
                
                if c == '\n':
                    rowPtr +=1
                    colPtr = 0
                    continue
                elif c == '.':
                    colPtr += 1
                    continue
                else:
                    symbols.append((rowPtr, colPtr))
                    colPtr += 1
                    continue
        else:
            if c.isdigit():
                parseNumFlag = True
                numString += c
                numStringCoords.append((rowPtr, colPtr))
                colPtr += 1
                continue
            else:
                if c == '\n':
                    rowPtr += 1
                    colPtr = 0
                    continue
                elif c == '.':
                    colPtr += 1
                    continue
                else: 
                    symbols.append((rowPtr, colPtr))
                    colPtr += 1
                    continue
    
    total = 0 

    for num, region in nums:
        for r, c in region: 
            if (r, c) in symbols:
                total += num
                break
    
    return total

def partTwo():
    file = open("Day_3_input.txt", "r").read()
    nums = []
    numCoords = []
    symbols = []
    rowPtr = 0
    colPtr = 0
    parseNumFlag = False
    numString = ""
    numStringCoords = []


    for c in file: 
        if parseNumFlag:
            if c.isdigit():
                numString += c
                numStringCoords.append((rowPtr, colPtr))
                colPtr += 1
                continue
            else:
                parseNumFlag = False
                nums.append((int(numString), getRegion(numStringCoords)))
                numString = ""
                numStringCoords = []
                
                
                if c == '\n':
                    rowPtr +=1
                    colPtr = 0
                    continue
                elif c == '.':
                    colPtr += 1
                    continue
                else:
                    symbols.append((c, rowPtr, colPtr))
                    colPtr += 1
                    continue
        else:
            if c.isdigit():
                parseNumFlag = True
                numString += c
                numStringCoords.append((rowPtr, colPtr))
                colPtr += 1
                continue
            else:
                if c == '\n':
                    rowPtr += 1
                    colPtr = 0
                    continue
                elif c == '.':
                    colPtr += 1
                    continue
                else: 
                    symbols.append((c, rowPtr, colPtr))
                    colPtr += 1
                    continue
    

    starPos = [(x[1], x[2]) for x in symbols if x[0] =='*']
    starNums = {}
    for num, region in nums: 
        for r, c in region:
            if (r, c) in starPos:
                if (r, c) in starNums: 
                    starNums[(r,c)].append(num)
                else:
                    starNums[(r,c)] = [num]
            continue
    
    total = 0
    for pos, l in starNums.items(): 
        if len(l) == 2:
            total += l[0] * l[1]
    
    return total

print(partOne())
print(partTwo())

                    


