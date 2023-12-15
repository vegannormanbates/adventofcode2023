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
platform = []
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        platform.append(list(line))
orig_platform = copy.deepcopy(platform)
platform = moveNorth(platform)
print('Part 1: ',calcLoad(platform))

platform = copy.deepcopy(orig_platform)
iterations = 1000000000
unique_arrangements = []
i = 0
repeat = False
while i < iterations:
    i += 1
    platform = spinCycle(platform)
    for arrangement in unique_arrangements:
        if set(map(tuple,arrangement)) == set(map(tuple,platform)) and repeat == False:
            repeat = True
            frequency =  i - unique_arrangements.index(arrangement)
            iterations = ((iterations - i) % (frequency-1)) + unique_arrangements.index(arrangement)
            print('Part 2: ',calcLoad(unique_arrangements[iterations]))
            break
    if repeat == False:
        unique_arrangements.append(platform)