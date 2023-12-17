# Day 13

def getGrid(str):
    return [list(s) for s in str.split('\n')]

def lineMatch(l1, l2, tolerance):
    misses = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            misses += 1 
        if misses > tolerance:
            return False
    return True

def partOne():
    file = open("Day_13_input.txt", "r")

    grids = [getGrid(s) for s in file.read().split('\n\n')]
    print(len(grids))
    total = 0
    loop = 0
    # print(grids[39])
    for g in grids: 
        loop += 1
        rows, cols = len(g), len(g[0])
        # Get row reflection pt: 

        rrps = []
        for r in range(1, rows):
            if lineMatch(g[r], g[r-1], 0):
                rrps.append(r)
        # print("rrp",rrp, loop)
        contMain = False
        for rrp in rrps:  
            # Check mirroring 
            lp, rp = rrp - 1, rrp 
            while lp >= 0 and rp < rows:
                if not lineMatch(g[lp], g[rp], 0):
                    break
                lp -= 1
                rp += 1
            # if lp or rp tipped over then all corres. lines were correctly mirrored 
            if lp < 0 or rp >= rows: 
                print("Grid:", loop, "row refl", rrp)
                total += rrp * 100
                contMain = True
                break 
        if contMain: 
            continue
        
        # If we reach here then there was no valid row refl.
        # Get col refletion pt: 
        crps = []
        for c in range(1, cols):
            if lineMatch([r[c] for r in g], [r[c-1] for r in g], 0):
                crps.append(c)
                
        # print("crp",crp, loop)
        # Check mirroring 
        for crp in crps: 
            lp, rp = crp - 1, crp
            # print(g)
            while lp >= 0 and rp < cols:
                # print([r[lp] for r in g])
                # print([r[rp] for r in g])
                if not lineMatch([r[lp] for r in g], [r[rp] for r in g], 0):
                    break
                lp -= 1
                rp += 1
            # if lp or rp tipped over then all corres. lines were correctly mirrored 
            if lp < 0 or rp >= cols: 
                print("Grid:", loop, "col refl", crp)
                # print("here2", crp)
                total += crp
                break 

    return total

def partTwo():
    file = open("Day_13_input.txt", "r")

    grids = [getGrid(s) for s in file.read().split('\n\n')]
    print(len(grids))
    total = 0
    loop = 0
    # print(grids[39])
    for g in grids: 
        loop += 1
        rows, cols = len(g), len(g[0])
        # Get row reflection pt: 

        rrps = []
        for r in range(1, rows):
            if lineMatch(g[r], g[r-1], 1):
                rrps.append(r)
        # print("rrp",rrp, loop)
        contMain = False
        for rrp in rrps:  
            # Check mirroring 
            lp, rp = rrp - 1, rrp 
            missed = False
            while lp >= 0 and rp < rows:
                if not lineMatch(g[lp], g[rp], 0):
                    if not missed and lineMatch(g[lp], g[rp], 1): 
                        missed = True 
                    else: 
                        break
                lp -= 1
                rp += 1
            # if lp or rp tipped over then all corres. lines were correctly mirrored 
            # need to check if a correction was made (missed == True)
            if missed and (lp < 0 or rp >= rows): 
                print("Grid:", loop, "row refl", rrp)
                total += rrp * 100
                contMain = True
                break 
        if contMain: 
            continue
        
        # If we reach here then there was no valid row refl.
        # Get col refletion pt: 
        crps = []
        for c in range(1, cols):
            if lineMatch([r[c] for r in g], [r[c-1] for r in g], 1):
                crps.append(c)
                
        # print("crp",crp, loop)
        # Check mirroring 
        for crp in crps: 
            lp, rp = crp - 1, crp
            missed = False 
            # print(g)
            while lp >= 0 and rp < cols:
                # print([r[lp] for r in g])
                # print([r[rp] for r in g])
                if not lineMatch([r[lp] for r in g], [r[rp] for r in g], 0):
                    if not missed and lineMatch([r[lp] for r in g], [r[rp] for r in g], 1):
                        missed = True
                    else: 
                        break 
                lp -= 1
                rp += 1
            # if lp or rp tipped over then all corres. lines were correctly mirrored 
            if missed and (lp < 0 or rp >= cols): 
                print("Grid:", loop, "col refl", crp)
                # print("here2", crp)
                total += crp
                break 

    return total
print(partOne())
print(partTwo())