#!/usr/bin/python
#Advent of Code 2023 Day 16

def beamTracer(Lbeams,layout):
    min_x = 0
    max_x = len(layout)
    min_y = 0
    max_y = len(layout[0])
    energized = []
    visited = [] #Need to track if I've already had a beam enter a space from the same direction
    for Lbeam in Lbeams:
        cur_x, cur_y, direction = Lbeam
        if energized.count(str(cur_x)+','+str(cur_y)) == 0 and cur_x >= min_x and cur_x < max_x and cur_y >= min_y and cur_y < max_y:
            energized.append(str(cur_x)+ ',' + str(cur_y))
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
                            Lbeams.append([cur_x+1,cur_y,'down'])
                            cur_x -=1
                        case 'right':
                            direction = 'up'
                            Lbeams.append([cur_x+1,cur_y,'down'])
                            cur_x -= 1
                case '-':
                    match direction:
                        case 'up':
                            direction = 'right'
                            Lbeams.append([cur_x,cur_y-1,'left'])
                            cur_y += 1
                        case 'down':
                            direction = 'right'
                            Lbeams.append([cur_x,cur_y-1,'left'])
                            cur_y += 1
                        case 'right':
                            cur_y += 1
                        case 'left':
                            cur_y -= 1
            if energized.count(str(cur_x)+','+str(cur_y)) == 0 and cur_x >= min_x and cur_x < max_x and cur_y >= min_y and cur_y < max_y:
                energized.append(str(cur_x)+',' + str(cur_y))
    return len(energized)



layout = []
beams = [[0,0,'right']]

with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        layout.append(list(line))

print('Part 1: ', beamTracer(beams,layout)) #This passes the example set, and every example input I can find - but fails on my real input data 'too low - I wasn't
# accounting for overlapping strings of x+y -had to had a splitter in the string

beams = []
max_x = len(layout)
max_y = len(layout[0])
beams = (
    [(x,0,'right') for x in range(len(layout))] +
    [(0,y,'down') for y in range(len(layout[0]))] +
    [(x,max_y-1,'left') for x in range(len(layout))] +
    [(max_x-1,y,'up') for y in range(len(layout[0]))]
)
max_energized = 0
for beam in beams:
    energized = beamTracer([beam],layout)
    if energized > max_energized:
        max_energized = energized

print('Part 2: ',max_energized)