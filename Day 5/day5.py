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

def rangeMaker(strt, end, dst_strt, dst_end):
    left = (strt,min(end,dst_strt))
    overlap = (max(strt,dst_strt),min(end,dst_end))
    right = (max(dst_end,strt),end)
    temp_rng = []
    overlaps = []

    if left[1] > left[0]:
        temp_rng.append(left)
    elif overlap[1] > overlap[0]:
        overlaps.append((dst_strt +(overlap[0]-strt),dst_strt + (overlap[1]-strt)))
    elif right[1] > right[0]:
        temp_rng.append(right)
    return overlaps 
        


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
for x in seeds[::2]:
    if index +1 <= len(seeds):
        strt = x
        end = x + seeds[index+1]
        seed_rngs.append([strt, end])
overlaps =[]

for rng in seed_rngs:
    for soil_rng in maps[0]:
        overlap= rangeMaker(rng[0],rng[1], soil_rng[0], soil_rng[1])
        #print(overlap)
        if len(overlap) > 0:
            overlaps.append(overlap[0])
locations2 = []
print (overlaps)
for x,y in overlaps:
    for i in range(x,y):
        locations2.append(rangeFinder(i))

print("Part 2: ", min(locations2))



#print(seed_rngs)

#Graveyard of bad ideas - all failed because they just wanted to try all of the seeds.
# seed_rngs = []
# index = 0
# for x in seeds[::2]:
#      if index + 1 <= len(seeds):
#          for y in range(x,x + seeds[index+1]):
#              seed_rngs.append(y)
#      index += 2

# for location in range(0,9999999999):
#     seed = revRangeFinder(location)
#     if seed in seed_rngs:
#         print ("Part 2:", location)
#         break

# works great on sample data. Crashes after using 57gb of memory on my macbook
# seed_rngs = []
# index = 0
# for x in seeds[::2]:
#     if index + 1 <= len(seeds):
#         for y in range(x,x + seeds[index+1]):
#             seed_rngs.append(y)
#     index += 2
# prt2_locations = []
# for x in seed_rngs:
#         prt2_locations.append(rangeFinder(x))
#  print('Part 2: ', min(prt2_locations))

#lets try just looking at a bunch of random points and see if there are any trends

# seed_limits = range(3660685134,3660685334,1)
# #test = [set(seed_limits) & set(seed_rngs)]
# test = seed_limits
# prt2_locations = []
# for x in test:
#     loc = rangeFinder(x)
#     if loc != x:
#         prt2_locations.append(loc)
#         print ("Rangefinder:", x,"Location:",loc )
# print (min(prt2_locations))