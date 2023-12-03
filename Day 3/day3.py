#!/usr/bin/python
#Advent of Code 2023 Day 3

import re #Regex here we go....

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

#Check for neighboring digits.
for coords in digit_locations:
    print ("Coords: ", coords["x"], coords["y"])
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
print("Part Numbers: ", part_nums)
print ("Sum of Part Numbers: ",sum(part_nums))
