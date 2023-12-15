#!/usr/bin/python
#Advent of Code 2023 Day 15

def hashAlg(step):
    cur_val = 0
    for char in step:
        cur_val += ord(char)
        cur_val = cur_val * 17
        cur_val = cur_val % 256
    return cur_val

init_seq = []
with open("input", "r") as txt:
    for line in txt:
        line = line.strip()
        init_seq = line.split(',')
values = []
for seq in init_seq:
    values.append(hashAlg(seq))

print('Part 1: ',sum(values))
boxes=[]
for i in range(256):
    boxes.append([])

for seq in init_seq:
    if '-' in seq:
        operator = '-'
    elif '=' in seq:
        operator = '='
    box_id = seq.split(operator)[0]
    if operator == '=':
        unique = True
        for i, lens in enumerate(boxes[hashAlg(box_id)]):
            lens_label = lens.split(operator)[0]
            if lens_label == box_id:
                boxes[hashAlg(box_id)].insert(i,seq)
                boxes[hashAlg(box_id)].pop(i+1)
                unique = False
        if unique == True:
            boxes[hashAlg(box_id)].append(seq)
    elif operator == '-':
        for i, lens in enumerate(boxes[hashAlg(box_id)]):
            lens_label = lens.split('=')[0]
            if lens_label == box_id:
                boxes[hashAlg(box_id)].pop(i)
focus_pwr = 0
for i,box in enumerate(boxes):
    for j, lens in enumerate(box):
        focal_length = int(lens[-1])
        focus_pwr += ((1+i)*(1+j)*focal_length)
print("Part 2: ", focus_pwr)