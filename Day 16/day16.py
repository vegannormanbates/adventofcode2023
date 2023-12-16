#!/usr/bin/python
#Advent of Code 2023 Day 16

layout = []
beams = [[0,0,'right']]

with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        layout.append(list(line))

min_x = 0
max_x = len(layout)
min_y = 0
max_y = len(layout[0])
energized = []
visited = [] #Need to track if I've already had a beam enter a space from the same direction

for beam in beams:
    cur_x, cur_y, direction = beam
    if energized.count(str(cur_x)+str(cur_y)) == 0 and cur_x >= min_x and cur_x < max_x and cur_y >= min_y and cur_y < max_y:
        energized.append(str(cur_x) + str(cur_y))
    print('Beam:',beam)
    while cur_x >= min_x and cur_x < max_x and cur_y >= min_y and cur_y < max_y:
        cur_char = layout[cur_x][cur_y]
        if [cur_x,cur_y,direction] not in visited:
            visited.append([cur_x,cur_y,direction])
        else:
            break
        match cur_char:
            case '.':
                match direction:
                    case 'right':
                        cur_y += 1
                    case 'left':
                        cur_y -= 1
                    case 'up':
                        cur_x -= 1
                    case 'down':
                        cur_x += 1
            case '\\':
                match direction:
                    case 'right':
                        direction = 'down'
                        cur_x += 1
                    case 'left':
                        direction = 'up'
                        cur_x -= 1
                    case 'down':
                        direction = 'right'
                        cur_y += 1
                    case 'up':
                        direction = 'left'
                        cur_y -= 1
            case '/':
                match direction:
                    case 'right':
                        direction = 'up'
                        cur_x -= 1
                    case 'left':
                        direction = 'down'
                        cur_x += 1
                    case 'down':
                        direction = 'left'
                        cur_y -= 1
                    case 'up':
                        direction = 'right'
                        cur_y += 1
            case '|':
                match direction:
                    case 'up':
                        cur_x -= 1
                    case 'down':
                        cur_x += 1
                    case 'left':
                        direction = 'up'
                        cur_x -=1
                        beams.append([cur_x+1,cur_y,'down'])
                    case 'right':
                        direction = 'up'
                        cur_x -= 1
                        beams.append([cur_x+1,cur_y,'down'])
            case '-':
                match direction:
                    case 'up':
                        direction = 'right'
                        cur_y += 1
                        beams.append([cur_x,cur_y-1,'left'])
                    case 'down':
                        direction = 'right'
                        cur_y += 1
                        beams.append([cur_x,cur_y-1,'left'])
                    case 'right':
                        cur_y += 1
                    case 'left':
                        cur_y -= 1
        if energized.count(str(cur_x)+str(cur_y)) == 0 and cur_x >= min_x and cur_x < max_x and cur_y >= min_y and cur_y < max_y:
            energized.append(str(cur_x) + str(cur_y))
        print('Currently at: ', cur_x, ',', cur_y)
print('Part 1: ', len(energized)) #This passes the example set, and every example input I can find - but fails on my real input data
#print('Whats energized:',energized)