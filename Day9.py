# Day 9

def partOne(post):
    
    def getNext(seq):
        diffSeq = [seq[i] - seq[i-1] for i in range(1,len(seq))]
        if all(x == 0 for x in diffSeq):
            return seq[-1]

        return seq[-1] + getNext(diffSeq)

    file = open("Day_9_input.txt", "r")

    total = 0 
    for line in file.readlines():
        lst = list(map(lambda x: int(x), line.split()))
        if not post:
            lst.reverse()
        total += getNext(lst)

    file.close()
    return total

def partTwo():
    return partOne(False)

print(partOne(True))
print(partTwo())