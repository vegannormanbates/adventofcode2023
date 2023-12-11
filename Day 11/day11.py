#!/usr/bin/python
#Advent of Code 2023 Day 11
import copy
from itertools import combinations

def findGalaxies(space):
    galaxies = []
    for x, row in enumerate(space):
        for y, col in enumerate(row):
            if col == '#':
                galaxies.append([x,y])
    return galaxies


space = [] 
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        space.append(list(line))
expansion = 1
galaxies = findGalaxies(space)
original_galaxies = copy.deepcopy(galaxies)
count = 0
space2 = copy.deepcopy(space) #making a copy to prevent infiinite looping
for x, row in enumerate(space2):
    max_row = len(space2)
    max_col = len(space2[0])
    if x not in (galaxy[0] for galaxy in galaxies):
        filler= []
        for y in range(max_col):
            filler.append('.')
        space.insert(x+count,filler)
        count+=1

space2 = copy.deepcopy(space) #making a copy to prevent infiinite looping
galaxies = findGalaxies(space)
space2 = list(zip(*space2))
space3 = copy.deepcopy(space2)
count = 0
for x, row in enumerate(space3):
    max_row = len(space3)
    max_col = len(space3[0])
    if x not in (galaxy[1] for galaxy in galaxies):
        filler= []
        for y in range(max_col):
            filler.append('.')
        space2.insert(x+count,filler)
        count +=1
space2 =list(zip(*space2))
space = space2
galaxies = findGalaxies(space)
distances = []
for x,y in combinations(galaxies,2):
    distance = abs(y[0] - x[0]) + abs(y[1] - x[1])
    distances.append(distance)
    count += 1
print ('Part 1:', sum(distances))
distances = []
expansion = 999999
expanded = []
for i, old in enumerate(original_galaxies):
    print ("Comparing: ", old,"to",galaxies[i])
    x = abs(galaxies[i][0] - old[0]) * expansion
    y = abs(galaxies[i][1] - old[1]) * expansion
    print('new: ', x,y)
    expanded.append([old[0]+x,old[1]+y])

for x,y in combinations(expanded,2):
    distance = abs(y[0] - x[0]) + abs(y[1] - x[1])
    distances.append(distance)
print ('Part 2: ', sum(distances))