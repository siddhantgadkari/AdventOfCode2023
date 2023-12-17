# Day 11
# pickleable 
from collections import defaultdict

def partOne():
    file = open("Day_11_input.txt", "r")
    gRow, gCol = set(), set()
    galaxies = []
    rows, cols = 0, 0
    for c in file.read():
        print(c)
        if c == '\n': 
            rows += 1
            cols = 0
            print(rows)
            continue
        if c == '#':
            gRow.add(rows)
            gCol.add(cols)
            galaxies.append([rows, cols])
        cols += 1
    rows += 1
    print("r", rows)
    print(cols)
    colShift = [0] * cols 
    rowShift = [0] * rows 
    print(gRow, gCol)
    for i in range(rows):
        if i not in gRow: 
            for j in range(i):
                rowShift[j] -= 999999
    for i in range(cols):
        if i not in gCol: 
            for j in range(i):
                colShift[j] -= 999999
    print(rowShift, colShift)
    for i in range(len(galaxies)):
        row, col = galaxies[i][0], galaxies[i][1]
        galaxies[i][0] += rowShift[row]
        galaxies[i][1] += colShift[col]
    
    total = 0
    for i in range(len(galaxies) - 1):
        r1, c1 = galaxies[i][0], galaxies[i][1]
        for j in range(i + 1, len(galaxies)):
            r2, c2 = galaxies[j][0], galaxies[j][1]
            total += abs(r1-r2) + abs(c1-c2)
    
    return total 

print(partOne())

