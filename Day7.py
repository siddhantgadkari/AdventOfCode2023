from collections import defaultdict
def listify(s):
    conversion = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    return sorted([int(c) if c.isdigit() else conversion[c] for c in s])

def getType(hand):
    cards = defaultdict(int)
    for c in hand: 
        cards[c] += 1
    
    if len(cards) == 1:
        return (("5oak", list(cards.keys())[0], 0))
    if len(cards) == 2:
        if list(cards.keys())[0] == 1:
            return(("4oak", list(cards.keys())[1], list(cards.keys())[0]))
        elif list(cards.keys())[0] == 4:
            return(("4oak", list(cards.keys())[0], list(cards.keys())[1]))
        elif list(cards.keys())[0] == 2:
            return (("fh", list(cards.keys())[1], list(cards.keys())[0]))
        else:
            return (("fh", list(cards.keys())[0], list(cards.keys())[1]))
    if len(cards) == 3:
        if 3 in cards.values():
            for c, f in cards.items(): 
                if f == 3:
                    return(("3oak", c, 0))
        else:
            pairs = [x[0] for x in cards.items() if x[1] == 2]
            return(("2p", max(pairs), min(pairs)))
    if len(cards) == 4:
        for c, f in cards.items():
            if f == 2:
                return(("1p", c, 0))
    return (("hc", max(list(cards.keys())), 0))



def partOne():
    file = open("Day_7_test_input.txt", "r")
    allHands = defaultdict(list)
    for line in file.readlines():
        line = line.split()
        hand, bid = getType(listify(line[0])), int(line[1])
        allHands[hand[0]].append((hand[1], hand[2], bid))
    winnings = 0
    totalHands = sum([len(x) for x in allHands.values()])
    for handType in ["5oak", "4oak", "fh", "3oak", "2p", "1p", "hc"]:
        for h in sorted(allHands[handType], reverse=True, key=lambda x: (x[0], x[1])):
            winnings += totalHands * h[2]
            totalHands -= 1
    file.close()
    return winnings

print(partOne())
