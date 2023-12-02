#!/usr/bin/python
#Advent of Code 2023 Day 2

max_red = 12
max_green = 13
max_blue = 14
possible_game_ids = []
power = 0 
with open("input", "r") as input:
    for line in input:
        game_id = ((line.split(':'))[0]).split()[1] #this mess gets the game ID.
        game = line.split(':')[1] # Gets everything after the game ID.
        hand_possible = 0
        min_red = 0
        min_green = 0
        min_blue = 0
        #Part 2 loop
        for handful in game.split(';'):
            cubes = handful.split(',')
            cube_possible = 0
            for cube in cubes:
                color = cube.split()[1]
                number = int(cube.split()[0])
                if color == 'red' and number > min_red:
                    min_red = number
                if color == 'green' and number > min_green:
                    min_green = number
                if color == 'blue' and number > min_blue:
                    min_blue = number            
        power = power + (min_red * min_blue * min_green)
        #Part 1 loop
        for handful in game.split(';'):
            cubes = handful.split(',')
            cube_possible = 0
            for cube in cubes:
                color = cube.split()[1]
                number = int(cube.split()[0])                    
                if color == 'red' and number > max_red:
                    break
                if color == 'green' and number > max_green:
                    break
                if color == 'blue' and number > max_blue:
                    break
                else:
                    cube_possible = cube_possible + 1
            if cube_possible == (len(cubes)):
                hand_possible = hand_possible + 1
        if hand_possible == len(game.split(';')):
            possible_game_ids.append(int(game_id))

print("Part 1: ",sum(possible_game_ids))
print("Part 2: ", power)