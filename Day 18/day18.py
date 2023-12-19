#!/usr/bin/python
#Advent of Code 2023 Day 18
#Todays Puzzle is literally how I solved day 10 - mostly a copy & paste job
vertices = []
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        directions = line.split()
        vertices.append(directions)

coordinates = [[0,0]]
perimeter = 0
for i, vertex in enumerate(vertices):
    cur_x, cur_y = coordinates[i]
    match vertex[0]:
        case 'R':
            cur_y += int(vertex[1])
        case 'L':
            cur_y -= int(vertex[1])
        case 'D':
            cur_x += int(vertex[1])
        case 'U':
            cur_x -= int(vertex[1])
    coordinates.append([cur_x,cur_y])
    perimeter+= int(vertex[1])

area = 0
for x,y in zip(coordinates,coordinates[1:]):
    area += (x[0]*y[1]) -(x[1]*y[0])
area = area / 2
area = abs(area)
area = area + perimeter/2 + 1
print ("Part 1:",area)

#part 2
coordinates = [[0,0]]
perimeter = 0
for i, vertex in enumerate(vertices):
    hex_string = vertex[2].strip('(')
    hex_string = hex_string.strip(')')
    hex_string = hex_string.strip('#')
    dir = hex_string[-1]
    hex_string = hex_string[:-1]
    value = int(hex_string,16)
    match dir:
        case '0':
            cur_y += value
        case '2':
            cur_y -= value
        case '1':
            cur_x += value
        case '3':
            cur_x -= value
    coordinates.append([cur_x,cur_y])
    perimeter+= value

area = 0
for x,y in zip(coordinates,coordinates[1:]):
    area += (x[0]*y[1]) -(x[1]*y[0])
area = area / 2
area = abs(area)
area = area + perimeter/2 + 1
print ("Part 2:",area)