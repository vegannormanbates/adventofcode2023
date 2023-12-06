#!/usr/bin/python
#Advent of Code 2023 Day 6


times = []
distances = []
with open("input", "r") as input:
        for line in input:
            line.strip() # no new lines.
            if line.startswith('Time:'):
                    line = line.split(':')[1]
                    times = line.split()
            if line.startswith('Distance:'):
                   line = line.split(':')[1]
                   distances = line.split()

wins = []
for i, time in enumerate(times):
        distance = int(distances[i])
        time = int(time)
        pressed = 0
        win = 0
        while pressed <= time:
            if((time - pressed) * pressed > distance):
                win += 1
            pressed += 1
        wins.append(win)

win_product = 1
for i in wins:
      win_product *= i
print("Part 1: ", win_product)

#Part 2 - There can only be one.
time = ''
for i in times:
      time += i
distance = ''
for i in distances:
      distance += i

distance = int(distance)
time = int(time)
pressed = 0
win = 0
while pressed <= time:
    if((time - pressed) * pressed > distance):
        win += 1
    pressed += 1
print("Part 2: ", win)