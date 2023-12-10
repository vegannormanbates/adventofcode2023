#!/usr/bin/python
#Advent of Code 2023 Day 10
#Finding the starting coordinates
def findStart(field):
    for x, row in enumerate(field):
        for y, col in enumerate(row):
            if col == 'S':
                return [x,y]
#Find the connecting Pipes For some reason I thought I would have to reuse this code more....
def firstPipe(coord,field):
    con_up = (field[coord[0]-1][coord[1]] in ['|','7','F'])
    con_down = (field[coord[0]+1][coord[1]] in ['|','L','J'])
    con_right = (field[coord[0]][coord[1]+1] in ['-','7','J'])
    con_left = (field[coord[0]][coord[1]-1] in ['-','L','F'])
    if con_up == True:
        return [-1, 0]
    elif con_down == True:
        return [1,0]
    elif con_right == True:
        return [0,1]
    elif con_left == True:
        return [0,-1] 
# Mapes the moves from each pipe type [0] is from top/right while [1] is bottom/left connect
moves = {
    '|' : [(1,0),(-1,0)] ,
    '-' : [(0,-1),(0,1)],
    'L' : [(0,1),(-1,0)],
    'J' : [(0,-1),(-1,0)],
    '7' : [(1,0),(0,-1)],
    'F' : [(1,0),(0,1)]
}
field = [] 
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        field.append(list(line))
start = findStart(field)
last_move = firstPipe(start,field)
cur_pos  = [start[0] + last_move[0],start[1] + last_move[1]]
steps = 1
path = []
path.append(start)
path.append(cur_pos)
while(cur_pos != start):
    cur_pipe = field[cur_pos[0]][cur_pos[1]]
    field[cur_pos[0]][cur_pos[1]] = str(steps)
    match last_move:
        case [-1,0]: #Bottom
            mv_idx  = 1
        case [1,0]: #Top
            mv_idx = 0
        case [0,1]: #Left
            mv_idx = 1
            if cur_pipe == '7':
                mv_idx = 0
        case [0,-1]: #Right
            mv_idx = 0
            if cur_pipe == 'L':
                mv_idx = 1
    cur_move = moves[cur_pipe][mv_idx]
    cur_pos = [cur_pos[0]+cur_move[0],cur_pos[1] + cur_move[1]]
    path.append(cur_pos)
    last_move = cur_move
    steps += 1
print ("Part 1: ",steps/2)
# https://www.themathdoctors.org/polygon-coordinates-and-areas/ something about shoelaces!?
area = 0
for x,y in zip(path,path[1:]):
    area += (x[0]*y[1]) -(x[1]*y[0])
area = area / 2
# This made an area that was too large.....also depending on which way you  go through the points you get a negative area lmao
area = abs(area)
# https://en.wikipedia.org/wiki/Pick%27s_theorem - guess I can try to use to remove the line from the area. MATH!
area = area - len(path)/2 +1
print ("Part 2: ", area) #I rounded the area up.....