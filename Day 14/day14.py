#!/usr/bin/python
#Advent of Code 2023 Day 14
import copy

def moveNorth(platform):
    platform = list(zip(*platform)) #rotate the platform
    for idx, row in enumerate(platform):
        row = list(row)
        cubes = []
        rounds = []
        for i, char in enumerate (row):
            if char == '#':
                cubes.append(i)
            if char == 'O':
                rounds.append(i)
        for round in rounds:
            if round == 0:
                continue #Can't move further north
            cube = [i for i in cubes if i < round] #Finds the first cube the round will hit
            if cube == []:
                cube = -1
            else:
                cube = max(cube) +1
            empty = row.index('.')
            move = max(empty, cube)
            if round > move:
                row.insert(move,row.pop(round)) # missing a condition on stacking multiples Os after a # but the way this processes it works
        platform[idx] = row
    return list(zip(*platform))

def moveSouth(platform):
    platform = list(zip(*platform)) #rotate the platform
    for idx, row in enumerate(platform):
        row = list(row)
        row.reverse()
        cubes = []
        rounds = []
        for i, char in enumerate (row):
            if char == '#':
                cubes.append(i)
            if char == 'O':
                rounds.append(i)
        for round in rounds:
            if round == 0:
                continue #Can't move further north
            cube = [i for i in cubes if i < round] #Finds the first cube the round will hit
            if cube == []:
                cube = -1
            else:
                cube = max(cube) +1
            empty = row.index('.')
            move = max(empty, cube)
            if round > move:
                row.insert(move,row.pop(round)) # missing a condition on stacking multiples Os after a # but the way this processes it works
        row.reverse()
        platform[idx] = row
    return list(zip(*platform))

def moveWest(platform):
    for idx, row in enumerate(platform):
        row = list(row)
        cubes = []
        rounds = []
        for i, char in enumerate (row):
            if char == '#':
                cubes.append(i)
            if char == 'O':
                rounds.append(i)
        for round in rounds:
            if round == 0:
                continue #Can't move further north
            cube = [i for i in cubes if i < round] #Finds the first cube the round will hit
            if cube == []:
                cube = -1
            else:
                cube = max(cube) +1
            empty = row.index('.')
            move = max(empty, cube)
            if round > move:
                row.insert(move,row.pop(round)) # missing a condition on stacking multiples Os after a # but the way this processes it works
        platform[idx] = row
    return platform

def moveEast(platform):
    for idx, row in enumerate(platform):
        row = list(row)
        row.reverse()
        cubes = []
        rounds = []
        for i, char in enumerate (row):
            if char == '#':
                cubes.append(i)
            if char == 'O':
                rounds.append(i)
        for round in rounds:
            if round == 0:
                continue #Can't move further north
            cube = [i for i in cubes if i < round] #Finds the first cube the round will hit
            if cube == []:
                cube = -1
            else:
                cube = max(cube) +1
            empty = row.index('.')
            move = max(empty, cube)
            if round > move:
                row.insert(move,row.pop(round)) # missing a condition on stacking multiples Os after a # but the way this processes it works
        row.reverse()
        platform[idx] = row
    return platform

def spinCycle(platform):
    platform = moveNorth(platform)
    platform = moveWest(platform)
    platform = moveSouth(platform)
    platform = moveEast(platform)
    return platform
def calcLoad(platform):
    rows = len(platform)
    load = 0
    for row in platform:
        rounds = row.count('O')
        load += rounds * rows
        rows -= 1
    return load
def findCycle(platform):
    unique_arrangements = []
    count = 0
    while True:
        platform = spinCycle(platform)
        repeat = False
        cycle_start = 0
        for j, arrangement in enumerate(unique_arrangements):
            if set(map(tuple,arrangement)) == set(map(tuple,platform)):
                repeat = True
                cycle_start = j
        if repeat == False:
            unique_arrangements.append(platform)
            count+= 1
        elif repeat == True:
            for i, arrangement in enumerate(unique_arrangements):
                print ("Arrangment ",i,": ", calcLoad(arrangement))
            return cycle_start, unique_arrangements

platform = []
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        platform.append(list(line))
orig_platform = copy.deepcopy(platform)
platform = moveNorth(platform)
print('Part 1: ',calcLoad(platform))

platform = copy.deepcopy(orig_platform)

# for i in range(10000):
#     print (i)
#     platform = spinCycle(platform)
#     repeat = False
#     print ('Load: ',calcLoad(platform))
#     for arrangement in unique_arrangements:
#         if set(map(tuple,arrangement)) == set(map(tuple,platform)):
#             print ('Repeat at: ',i)
#             repeat = True
#             repeat_index.append(i)
#             break
#     if repeat == False:
#         unique_arrangements.append(platform)
#     elif repeat == True:
#         break

# Need to find the cycle then get the load number for the arrangment we'd be at if running
# 1000000000 times.... This code works for the sample input but not the actual input.
cycle_start, platforms = findCycle(platform)
length = len(platforms) - (cycle_start)
iterations = ((1000000000 - cycle_start) % length) + cycle_start -1
print ('Iterations: ',iterations)
load = 0
print('Part 2: ',calcLoad(platforms[iterations]))