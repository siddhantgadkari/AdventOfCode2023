# Day 10 
from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
def partOne():
    loopMap = defaultdict(int)
    file = open("Day_10_input.txt", "r")
    pipeMap = []
    row, col = 0, 0
    for line in file.readlines():
        rowPipes, col = [], 0 
        for char in line.strip():
            if char == 'S':
                startPos = (row, col)
            rowPipes.append(char)
            col += 1
        pipeMap.append(rowPipes)
        row += 1
    print(pipeMap)
    """
            (-1, 0)
     (0, -1)   p   (0, 1)
             (1, 0)
    
    """

    inOutDirs = {'|':[(-1,0),(1,0)], 
                 '-':[(0, 1), (0, -1)], 
                 'L':[(-1, 0), (0, 1)], 
                 'J':[(-1, 0), (0, -1)], 
                 '7':[(0, -1), (1, 0)], 
                 'F':[(0, 1), (1, 0)]}

    def traversePipe(r, c, i, steps):
        print(pipeMap[r][c])
        if pipeMap[r][c] == 'S':
            return 
        if (r,c) in loopMap:
            loopMap[(r,c)] = min(loopMap[(r,c)], steps)
        else:
            loopMap[(r,c)] = steps 
        dr, dc = [x for x in inOutDirs[pipeMap[r][c]] if x != i][0]
        traversePipe(r+dr, c+dc, (-1 * dr, -1 * dc), steps + 1)
    
    dirs = [(-1,0), (1,0), (0, 1), (0, -1)]
    rows = len(pipeMap)
    cols = len(pipeMap[0])
    for dr, dc in dirs: 
        nextR, nextC = startPos[0] + dr, startPos[1] + dc
        if (0 <= nextR < rows and 
            0 <= nextC < cols and 
            pipeMap[nextR][nextC] != '.' and  
            (-1 * dr, -1 * dc) in inOutDirs[pipeMap[nextR][nextC]]):

            traversePipe(nextR, nextC, (-1 * dr, -1 * dc), 1)
    file.close()
    return max(loopMap.values())


print(partOne())