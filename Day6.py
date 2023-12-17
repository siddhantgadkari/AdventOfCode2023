# Day 6
def getDistTime():
    file = open("Day_6_input.txt", "r")
    lines = list(map(lambda x: x.split()[1:], file.readlines()))
    file.close()
    return (lines[1], lines[0])

def partOne(): 
    error = 1
    d, t = getDistTime()
    for i in range(len(d)):
        ways = 0
        for j in range(int(t[i]) + 1):
            if j * (int(t[i]) - j) > int(d[i]):
                ways += 1
        error *= ways
    return error

def partTwo():
    totalWays = 0
    d, t = getDistTime()
    d, t = int(''.join(d)), int(''.join(t))
    for i in range(t + 1):
        if i * (t - i) > d:
            totalWays += 1
    return totalWays


print(partOne())
print(partTwo())
