# Day 17

from queue import PriorityQueue

# checks if a coord is valid for a row, col matrix
def validCoord(rowCount, colCount, coord):
    r, c = coord
    if not (0 <= c < colCount and 0 <= r < rowCount):
        return False
    return True


def partOne():
    file = open("Day_17_test_input.txt", "r")
    grid = [list(map(int, list(line.strip()))) for line in file.readlines()]
    rows, cols = len(grid), len(grid[0])

    # q has: [(cost, (src, dst, linear moves)), ...]
    # linM is (count, direction string)
    # costs has: {dst : (src, cost), ...}
    costs, q = {}, PriorityQueue()
    q.put((0, ((0, 0), (0, 0), (1, "left"))))
    dirs = {"right":(0, 1), "left":(0, -1), "down":(1, 0), "up":(-1, 0)}
    while not q.empty():
        edge = q.get()
        cost = edge[0]
        src, dst, linM = edge[1]
        # put or update costs edge if needed
        if dst not in costs or cost < costs[dst][1]: 
            costs[dst] = (src, cost)
            print(costs)
        currR, currC = dst 
        for dir, move in dirs.items(): 
            dr, dc = move
            next = (currR + dr, currC + dc)
            if not validCoord(rows, cols, next) or next == src:
                continue
            # need to handle linear movement
            if dir == linM[1]:
                # node has come via 3 linear steps
                if linM[0] == 3:
                    continue
                q.put((grid[next[0]][next[1]], 
                       (dst, next, (linM[0] + 1, linM[1]))))
            else: 
                q.put((grid[next[0]][next[1]], 
                       (dst, next, (1, dir))))
        print(q)
    
    start = (0, 0)
    curr = (cols - 1, rows - 1)
    total = 0
    while curr != start: 
        curr, cost = costs[curr]
        total += cost
    file.close()
    return total 

print(partOne())