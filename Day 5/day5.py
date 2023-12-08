#!/usr/bin/python
#Advent of Code 2023 Day 5

seeds = []
maps = []
map_index = -1

def rangeFinder(x):
    for index in range(len(maps)):
        for srcMin, srcMax, dst in maps[index]:
            if srcMin <= x <= srcMax:
                x = dst + (x-srcMin)
                break
    return x

#Can we go backwards? Yes - but it doesn't actually help at all lol
def revRangeFinder(x): 
    for index in range(len(maps)-1,0,-1):
        for srcMin, srcMax, dst in maps[index]:
            rng = srcMax - srcMin #turns out I should have left this in the data
            if dst <= x < dst+rng:
                x = srcMin + (x-dst)
                break
    return x


with open("input", "r") as input:
    for line in input:
        line.strip() # no new lines.
        if line.startswith('seeds:'):
            for num in line.split()[1:]:
                seeds.append(int(num))
        elif line.endswith('map:\n'):
            map_index+= 1
            maps.append([])
            continue
        elif line[0].isdigit():
            dst, src, rng = [int(x) for x in line.split()] #pythong really wanted x to be a str :(
            # src start of source range
            # src+rng max of source range
            # dst - start of dst range - the next map will then have that rng defined.
            maps[map_index].append([src,(src+rng),dst])

locations = []
for x in seeds:
        locations.append(rangeFinder(x))
print("Part 1: ", min(locations))

#part 2 - seeds are now ranges?
index = 0
seed_rngs = []
locations2 =[]
for x in seeds[::2]:
    if index +1 <= len(seeds):
        strt = x
        end = x + seeds[index+1]
        test = [(strt, end)]
    for Map in maps:
        test = rangeMaker(test,Map)
    locations2.append(min(test))

print(locations2)
#Ranges are huge -need to narrow them. First attempt(s) at part2 through only lmited the first step from seeds.
# Need to implement a solution that finds ranges at each step.
