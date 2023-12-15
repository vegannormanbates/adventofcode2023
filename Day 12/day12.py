#!/usr/bin/python
#Advent of Code 2023 Day 12
from functools import cache
@cache #This seems like some kind of cheat code....

def find_order(records, strs):
    if len(records) == 0:
        if "#" in strs:
            return 0
        return 1
    curr = records[0]
    counts = 0
    for i in range(len(strs) - sum(records[1:])):
        for j in range(i, i + curr):
            if j == i and j > 0 and strs[j - 1] == "#":
                return counts
            if j >= len(strs):
                return counts
            if strs[j] == ".":
                break
            if j == i + curr - 1:
                if j + 1 < len(strs) and strs[j + 1] == "#":
                    break
                counts += find_order(records[1:], strs[j + 2 :])
    return counts

def unfolding (record, string):
    record = record * 5
    new_string = string
    for i in range(4):
        string += '?' + new_string
    return record, string

strs = []
records = []
strs2 = []
records2 = []
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        strs.append(line.split()[0])
        record = (line.split()[1].split(','))
        record = list(map(int,record))
        records.append(record)
arrangements = 0
for i, record in enumerate (records):
    arrangements += find_order(tuple(record),((strs[i])))
print ("Part 1:", arrangements)

for i, record in enumerate (records):
    records[i], strs[i] = unfolding(record, strs[i])
arrangements = 0 
for i, record in enumerate (records):
    arrangements += find_order(tuple(record),((strs[i])))
print("Part 2?", arrangements) 