#!/usr/bin/python
#Advent of Code 2023 Day 13

def findReflections(pattern, part):
    rows = len(pattern)
    cols = len(pattern[0])
    for i,row in enumerate(pattern):
        if i+1 < rows and smudgeFinder(row, pattern[i+1]) <= part:
            reflection = min(len(pattern[:i+1]),len(pattern[i+1:]))
            print ("Possible reflection at: ",i+1)
            print ("\tReflection: ",reflection)
            smudges = smudgeFinder(row, pattern[i+1])
            print("\tSmudges: ",smudges)
            if i+1 == 1:
                smudges = 0
            count = 0
            for j,k in zip(reversed(pattern[:i+1]), pattern[i+1:]):
                if smudgeFinder(j, k) + smudges <= part:
                    print ("\tCount: ",count+1)
                    count += 1
                    smudges += smudgeFinder(j, k)
                    if reflection == count and smudges == part:
                        return 100 * (i+1)
    pattern = list(zip(*pattern)) #Rotate the matrix
    for i,row in enumerate(pattern):
        if i+1 < cols and smudgeFinder(row, pattern[i+1]) <= part:
            reflection = min(len(pattern[:i+1]),len(pattern[i+1:]))
            print ("Possible Vert reflection at: ",i+1)
            print ("\tReflection: ",reflection)
            smudges = smudgeFinder(row, pattern[i+1])
            print("\tSmudges: ",smudges)
            if i+1 == 1:
                smudges = 0
            count = 0
            for j,k in zip(reversed(pattern[:i+1]), pattern[i+1:]):
                if smudgeFinder(j, k) + smudges <= part:
                    print ("\tCount: ",count+1)
                    count += 1
                    smudges += smudgeFinder(j, k)
                    print ("\tSmudges: ",smudges)
                    if reflection == count and smudges == part:
                        return i+1
    return 0

def smudgeFinder(str1, str2):
    count = sum(1 for x, y in zip(str1, str2) if x != y)
    return count
patterns = []
pat_num = 0
pattern = []
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        if len(line) == 0:
            pat_num+= 1
            patterns.append(pattern)
            pattern = []
        else:
            line = line.replace('.','0') #Switching to binary instead
            line = line.replace('#','1')
            pattern.append(line)
patterns.append(pattern)
part1 = 0
for pattern in patterns:
   part1+= findReflections(pattern, 0)
print("Part 1: " ,part1)
part2 = 0
for pattern in patterns:
    part2+= findReflections(pattern, 1) #Part 2 is still hella broken....
print ("Part 2: ", part2)