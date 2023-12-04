#!/usr/bin/python
#Advent of Code 2023 Day 3

import re #Regex here we go....
from itertools import product #Will do all the coordinate stuff for me.
import copy #TIL about variables and refernces default behavior in pythong
def get_adj_numbers(digit_locations, x, y):
    print("Checking Coords: ",x,y)
    for coords in digit_locations:
        if coords['x'] == x or coords['x'] == x - 1 or coords['x'] == x + 1:
            if coords['y'] == y or coords['y'] == y - 1 or coords['y'] == y + 1:
                print("Get Numbers returing: ",coords.get('number'))
                return coords.get('number')

#Reads the input data and saves it into a 2 dimensional list 
engine_schematics = []
with open("input", "r") as input:
    for line in input:
        line = line.strip()
        engine_schematics.append(list(line))

row_num = 0
max_row = len(engine_schematics)
max_col = len(engine_schematics[0]) #Assumes each row is equal length

# Finds the coordinates of all the digits in the data
digit_locations = []
for row in engine_schematics:
    col_num = 0
    while col_num < max_col:
        if (str(engine_schematics[row_num][col_num]).isdigit()):
            digit_locations.append({"x":row_num,"y":col_num,"adj": 0})
        col_num += 1
    row_num += 1

part_nums = []
row_num = 0 #Resetting Row Numbers
#Theoretically this determines if a number is a part number or not
for coords in digit_locations:
    neighbors = []
    if coords["x"] > 0 and coords["y"] > 0 and coords["x"] < max_row-1 and coords["y"] < max_col-1:
        if (re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]-1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]+1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]+1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]-1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]+1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]-1]) == None
        ):
            coords.update({"adj": 1})
    elif coords["x"] == 0 and coords["y"] > 0 and coords["x"] < max_row-1 and coords["y"] < max_col-1:
        if (
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]-1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]+1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]+1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]-1]) == None
        ):
            coords.update({"adj": 1})
    elif coords["x"] == 0 and coords["y"] == 0 and coords["x"] < max_row-1 and coords["y"] < max_col-1:
        if (
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]+1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]+1][coords["y"]+1]) == None
        ):
            coords.update({"adj": 1})
    elif coords["x"] > 0 and coords["y"] > 0 and coords["x"] == max_row-1 and coords["y"] < max_col-1:
        if (re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]-1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]+1])== None or
            re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]+1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]-1]) == None
        ):
            coords.update({"adj": 1})
    elif coords["x"] > 0 and coords["y"] > 0 and coords["x"] == max_row-1 and coords["y"] == max_col-1:
        if (re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]][coords["y"]-1]) == None or
            re.search(r'\.|\d', engine_schematics[coords["x"]-1][coords["y"]-1]) == None 
        ):
            coords.update({"adj": 1})
#I'm going to destroy eingine_schematics later instead of chanfing that lets waste memory
new_engine_schematics = copy.deepcopy(engine_schematics)

#Check for neighboring digits.
for coords in digit_locations:
    pos_num = ""
    if coords["adj"] == 1 and str(engine_schematics[coords["x"]][coords["y"]]).isdigit():
        pos_num = str(engine_schematics[coords["x"]][coords["y"]])
        if coords["y"] -1 >= 0 and str(engine_schematics[coords["x"]][coords["y"]-1]).isdigit():
            pos_num = str(engine_schematics[coords["x"]][coords["y"]-1]) + pos_num
            engine_schematics[coords["x"]][coords["y"]-1] = "."
            if coords["y"] -2 >= 0 and str(engine_schematics[coords["x"]][coords["y"]-2]).isdigit():
                pos_num = str(engine_schematics[coords["x"]][coords["y"]-2]) + pos_num
                engine_schematics[coords["x"]][coords["y"]-2] = "."
        if coords["y"] + 1 <= max_col -1  and str(engine_schematics[coords["x"]][coords["y"]+1]).isdigit():
            pos_num = pos_num + str(engine_schematics[coords["x"]][coords["y"]+1])
            engine_schematics[coords["x"]][coords["y"]+1] = "."
            if coords["y"] + 2 <= max_col -1 and str(engine_schematics[coords["x"]][coords["y"]+2]).isdigit():
                pos_num = pos_num + str(engine_schematics[coords["x"]][coords["y"]+2])
                engine_schematics[coords["x"]][coords["y"]+2] = "."    
    if str(pos_num).isdigit():
        part_nums.append(int(pos_num))
        coords["number"] = int(pos_num) 
print ("Sum of Part Numbers: ",sum(part_nums))

#Part 2 - I'm just throwing way all the garbage I did last night and approaching this completely differrently
engine_schematics = new_engine_schematics

gears = []
#Product basically does all the for loops from part 1 for me. Combining all the values from x and y automagically
for x,y in product(range(max_row),range(max_col)):
    if engine_schematics[x][y] == '*':
        gears.append([x,y])
adj = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1, -1), (1,0), (1,1)] #the relative coords of all the adjacent spaces
#now we need to find all the numbers near gears.
number_coords = []
for x,y in gears:
    temp_coords = []
    for a,b in adj:
        if engine_schematics[x+a][y+b].isnumeric():
            temp_coords.append([x+a,y+b])
    number_coords.append(temp_coords)

#We need to make sure we're not counting a single 'number' with multiple adj digits multiple times.
#number_coords = [[(x,y) for x,y in coord if (x,y-1) not in coord] for coord in number_coords]
new_coords = []
for adj in number_coords:
    temp = []
    for x,y in adj:
        if [x, y-1] not in adj:
            temp.append([x,y])
    new_coords.append(temp)
number_coords = new_coords

#Removes all the gears with only one adjacency. I assumed there would only ever be 2 and that worked in my input data lol
temp = []
for coords in number_coords: 
    if len(coords) == 2:
        temp.append(coords)
number_coords = temp
gear_ratio_sum  = 0
#Messy code again - identifies the full numbers. Assumes they're only ever going to be a max of 3 digits. Could probably write a recursive function
for gear in number_coords:
    gear_ratio = []
    ratio = 1
    for coords in gear:
        x = coords [0]
        y = coords [1]
        num = str(engine_schematics[x][y])
        if str(engine_schematics[x][y+1]).isdigit() and y+1 <= max_col-1:
            num = str(num) + str(engine_schematics[x][y+1])
            if str(engine_schematics[x][y+2]).isdigit() and y+2 <= max_col-1:
                num = str(num) + str(engine_schematics[x][y+2])
        if str(engine_schematics[x][y-1]).isdigit() and y-1 >= 0:
            num = str(engine_schematics[x][y-1]) + str(num)
            if str(engine_schematics[x][y-2]).isdigit() and y-2 >= 0:
                num = str(engine_schematics[x][y-2]) + str(num)
        gear_ratio.append(int(num))
    for num in gear_ratio:
        ratio = ratio * num
    gear_ratio_sum += ratio

print("Sum of Gear Ratios: ", gear_ratio_sum)