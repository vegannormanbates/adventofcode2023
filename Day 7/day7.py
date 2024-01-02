#!/usr/bin/python
#Advent of Code 2023 Day 7
from functools import cmp_to_key

def typeTuple (hand):
    counts = []
    for char in hand:
        counts.append(hand.count(char))
    counts.sort(reverse=True)
    return(counts)

def typeFinder (counts):
    if max(counts) == 5:
        #Five of a kind
        return 7
    elif max(counts) == 4:
        #Four of a kind
        return 6
    elif max (counts) == 3 and min(counts) == 2:
        #Full House
        return 5
    elif max (counts) == 3:
        #Three of a kind
        return 4
    elif max (counts) == 2 and counts.count(min(counts)) == 1:
        #Two Pair
        return 3
    elif max (counts) == 2 and counts.count(min(counts)) == 3:
        #One Pair
        return 2
    elif max(counts) == 1:
        #High Card
        return 1

def returnType(hand):
     return hand['type']

def charValue(char):
    #part 1 - SWAP THESE TO SWITCH BETWEEN PARTS
    #values = '23456789TJQKA'
    #part 2
    values = 'J23456789TQKA'
    return values.find(char)

def compHands(hand1, hand2):
     if hand1['type'] > hand2['type']:
        return 1
     elif hand1['type'] < hand2['type']:
        return -1
     elif hand1['type'] == hand2['type']:
        for i, char in enumerate(hand1['cards']):
            value1 = charValue(char)
            value2 = charValue(hand2['cards'][i])
            if value1 > value2:
                return 1
            elif value1 < value2:
                return -1

hands = []
with open("input", "r") as input:
        for line in input:
            hand = {}
            line.strip() # no new lines.
            h,b = line.split()
            hand['cards'] = h
            hand['tuple'] = typeTuple(h)
            hand['type'] = typeFinder(hand['tuple'])
            hand['bid'] = b
            hands.append(hand)
hands = sorted(hands,key=cmp_to_key(compHands))
total_winnings = 0
for i, hand in enumerate(hands):
    total_winnings += int(hand['bid']) * (i+1)
print("Part 1: ", total_winnings)

#Part 2 - will J always get more points?

for hand in hands:
    count = hand['cards'].count('J')
    if count > 0:
        if hand['type'] == 2 and count >=1:
            hand['type'] = 4
        elif hand['type'] == 3 and count == 2:
            hand['type'] = 6
        elif hand['type'] == 3 and count == 1:
            hand['type'] = 5
        elif hand['type'] == 4 and count ==1:
            hand['type'] = 6
        elif hand['type'] == 4 and count ==3:
            hand['type'] = 6
        elif hand['type'] + count <= 7:
            hand['type'] += count
        else:
            hand['type'] = 7
    
hands = sorted(hands,key=cmp_to_key(compHands))
total_winnings = 0
for i, hand in enumerate(hands):
    total_winnings += int(hand['bid']) * (i+1)
print("Part 2: ", total_winnings)