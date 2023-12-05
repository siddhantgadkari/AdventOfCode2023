#Day 1 

def partOne():
    file = open("Day_1_input.txt", "r")
    total = 0
    for s in file.readlines():
        lp, rp  = 0, len(s) - 1
        lFlag, rFlag = False, False
        while not (lFlag and rFlag):
            if s[lp].isdigit():
                lFlag = True
            else: 
                lp += 1
            
            if s[rp].isdigit():
                rFlag = True
            else: 
                rp -= 1
        total += int(s[lp] + s[rp])
        file.close()
    return total

def partTwo():
    digitMap = {"one"   : 1, 
                "two"   : 2, 
                "three" : 3, 
                "four"  : 4, 
                "five"  : 5, 
                "six"   : 6, 
                "seven" : 7, 
                "eight" : 8, 
                "nine"  : 9}
    
    file = open("Day_1_input.txt", "r")
    total = 0
    for s in file.readlines():
        lVal, rVal = 0, 0
        lString, rString = "", ""
        for c in s: 
            breakFlag = False
            for num in digitMap: 
                if num in lString:
                    lVal = digitMap[num]
                    breakFlag = True
                    break
            if breakFlag:
                break
            lString += c

            if c.isdigit():
                lVal = int(c)
                break
        
        for i in range(len(s) - 1, -1, -1):

            breakFlag = False
            for num in digitMap:
                if num in rString: 
                    rVal = digitMap[num]
                    breakFlag = True
                    break
            if breakFlag:
                break
            rString = s[i] + rString
            
            if s[i].isdigit():
                rVal = int(s[i])
                break
        total += lVal * 10 + rVal
    file.close()
    return total 
    
print(partOne())
print(partTwo())
    
