#!/usr/bin/python
#Advent of Code 2023 Day 9
from itertools import pairwise

def getNext(sequence):
    if set(sequence) == {0}: #Checks for all zeroes
        return 0
    differences = []
    for x,y in pairwise(sequence):
        difference = int(y) - int(x)
        differences.append(difference)
    final = getNext(differences)
    return int(sequence[-1]) + final

def getLast(sequence):
    if set(sequence) == {0}: #Checks for all zeroes
        return 0
    differences = []
    for x,y in pairwise(sequence):
        difference = int(y) - int(x)
        differences.append(difference)
    final = getLast(differences)
    return int(sequence[0]) - final

history = []
with open("input", "r") as input:
    for line in input:
        line = line.strip()
        history.append(line.split())
part1 = 0
part2 = 0
for sequence in history:
    part1 += getNext(sequence)
    part2 += getLast(sequence)


print ("Part 1: ", part1)
print ("Part 2: ", part2)
