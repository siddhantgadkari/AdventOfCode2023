# Day 5

def partOne():
    def getRanges(s):
        strRanges = s.split('\n')
        ranges = []
        for r in strRanges[:len(strRanges) - 1]: 
            imdt = r.split()
            ranges.append((int(imdt[0]), int(imdt[1]), int(imdt[2])))
        return ranges
    
    file = open("Day_5_input.txt", "r")
    lines = file.readlines()
    maps = []
    mapWriteMode = False
    currMapString = ""
    lcount = 0 
    while lcount < len(lines):
        currLine = lines[lcount]
        if lcount == 0: 
            seeds = [int(x) for x in lines[lcount].split()[1:]]
        if lcount == len(lines) - 1:
            currMapString += currLine
        if not currLine.strip() or lcount == len(lines) - 1:
            if mapWriteMode: 
                maps.append(getRanges(currMapString))
                mapWriteMode = False
                currMapString = ""

        if mapWriteMode:
            currMapString += currLine

        if "map" in currLine: 
            mapWriteMode = True
        lcount += 1

    def findId(idIn, ranges):
        for (dst, src, r) in ranges:
            if idIn in range(src, src + r):
                return dst + (idIn - src)
        return idIn
    
    locationIds = []
    for s in seeds: 
        id = s
        mcount = 0
        while mcount < len(maps):
            id = findId(id, maps[mcount])
            mcount += 1
        locationIds.append(id)
    return min(locationIds)
                    
def partTwo():
    def getRanges(s):
        strRanges = s.split('\n')
        ranges = []
        for r in strRanges[:len(strRanges) - 1]: 
            imdt = r.split()
            ranges.append((int(imdt[0]), int(imdt[1]), int(imdt[2])))
        return ranges
### CREATING INTERAL REPN ###    
    file = open("Day_5_input.txt", "r")
    lines = file.readlines()
    maps = []
    mapWriteMode = False
    currMapString = ""
    lcount = 0 
    while lcount < len(lines):
        currLine = lines[lcount]
        if lcount == 0: 
            seedsimdt = [int(x) for x in lines[lcount].split()[1:]]
            seedRanges = []
            for i in range(len(seedsimdt)):
                if i%2 == 0:
                    seedRanges.append((seedsimdt[i], seedsimdt[i] + seedsimdt[i+1]))
        if lcount == len(lines) - 1:
            currMapString += currLine
        if not currLine.strip() or lcount == len(lines) - 1:
            if mapWriteMode: 
                maps.append(getRanges(currMapString))
                mapWriteMode = False
                currMapString = ""
        if mapWriteMode:
            currMapString += currLine

        if "map" in currLine: 
            mapWriteMode = True
        lcount += 1
### CREATING INTERAL REPN ### 

    print(seedRanges)
    minLocations = []
    for sr in seedRanges[:1]:
        print(sr)
        mcount = 0
        processed, raw = [], [sr]
        while mcount < len(maps):
            mapRanges = maps[mcount]
            print(mapRanges)
            rangePtr = 0
            while raw: 

                currRangeStart, currRangeEnd = raw.pop()
                # if all ranges have been checked, there is no convertion available for thar range; simply shift the ranges as they are
                if rangePtr == len(mapRanges):
                    # print("RP ", processed)
                    # print("RP ", raw)
                    processed.append((currRangeStart, currRangeEnd))
                    rangePtr = 0
                    continue
                
                # # residue empty: 
                # if currRangeStart == 0 and currRangeEnd == 0:
                #     continue
                
                convStart, start, rlen = mapRanges[rangePtr]
                print(mapRanges[rangePtr])
                # can completely convert currRange; no residue
                if currRangeStart >= start and currRangeEnd <= start + rlen:
                    processed.append((convStart + (currRangeStart - start), convStart + (currRangeStart - start) + currRangeEnd - currRangeStart))
                # can partially convert only from left; right residue    
                elif currRangeStart >= start and currRangeStart < start + rlen < currRangeEnd:
                    processed.append((convStart + (currRangeStart - start), convStart + rlen))
                    raw.append((start + rlen, currRangeEnd))
                # can partially convert only from right; left residue
                elif currRangeStart < start < currRangeEnd and currRangeEnd <= start + rlen:
                    processed.append((convStart, convStart + (currRangeEnd - start)))
                    raw.append((currRangeStart, start))
                # only centre partial can be converted; left and right residues
                elif currRangeStart <= start and currRangeEnd >= start + rlen: 
                    processed.append((convStart, convStart + rlen))
                    raw.append((currRangeStart, start))
                    raw.append((start + rlen, currRangeEnd))
                # no conversion possible at all
                else:
                    raw.append((currRangeStart, currRangeEnd))
                # print("P ", processed)
                # print("R ", raw)
                rangePtr += 1
            # print("Pe ", processed)
            # print("Re ", raw)
            raw = processed
            processed = []
            print("end ", raw)
            mcount += 1
        minLocations.append(min([x[0] for x in raw]))
    return min(minLocations)




print("Lowest is: ", partTwo())