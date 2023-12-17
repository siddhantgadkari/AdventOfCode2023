# Day 15 
"""
This is so dumb:

label = "key"
d = dict(label = 2)
print(d)
>>> {'label' : 2}
"""

def getHash(str):
    curr = 0
    for c in str: 
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    return curr

def partOne():
    file = open("Day_15_input.txt", "r")
    total = 0
    for str in file.read().strip().split(','):
        total += getHash(str)

    file.close()
    return total

def partTwo():
    file = open("Day_15_input.txt", "r")
    #        hash {label : (pos, focal len), ... }
    #boxes = {0 = {"cd" : (1, 8), ...}, ...}
    boxes = {}
    for str in file.read().strip().split(','):
        print(str)
        # '=' instruction
        if str[-1].isdigit():
            label = str[:-2]
            fl = int(str[-1])
            box = getHash(label)
            print(box, label, fl)
            # box alr exists
            if box in boxes: 
                # label alr in box 
                if label in boxes[box]:
                    boxes[box][label] = (boxes[box][label][0], fl)
                # label not in box
                else:
                # box empty
                    if not boxes[box]:
                        boxes[box][label] = (0, fl)
                    # box has other labels
                    else: 
                        boxes[box][label] = (max(x[0] for x in boxes[box].values()) + 1, fl)
            # box doesn't exist
            else:
                boxes[box] = {}
                boxes[box][label] = (0, fl)
        # '-' instruction
        else:
            label = str[:-1]
            box = getHash(label)
            print(box, label)
            # box exists
            if box in boxes: 
                boxes[box].pop(label, None)
        print(boxes)
    total = 0
    for box, lenses in boxes.items(): 
        fps = [x[1] * (1 + box) for x in sorted(lenses.values(), key=lambda x: x[0])]
        for i in range(len(fps)):
            fps[i] *= (i + 1)
        total += sum(fps)
    file.close
    return total 

print(partTwo())