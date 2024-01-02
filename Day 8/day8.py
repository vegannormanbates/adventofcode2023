#!/usr/bin/python
#Advent of Code 2023 Day 8
from math import gcd
directions =[]
nodes = []
node_name = []

with open("input", "r") as input:
    for i,line in enumerate (input):
        line = line.strip()
        if i == 0:
            directions = list(line)
        elif len(line) == 0:
            continue
        else:
            node,line = line.split('=')
            line = line.replace('(','')
            line = line.replace(')','')
            left,right = line.split(',')
            node_name.append(node.strip())
            nodes.append([left.strip(),right.strip()])
steps = 0
current_node = 'AAA'

while current_node != 'ZZZ':
    index = (steps%len(directions))
    next_node = ''
    if directions[index] == 'L':
        next_node = nodes[node_name.index(current_node)][0]
    elif directions[index] == 'R':
        next_node = nodes[node_name.index(current_node)][1]
    current_node = node_name[node_name.index(next_node)]
    steps+= 1
print ('Part 1: ', steps)

a_nodes = []
for x, i in enumerate(node_name):
    if i.endswith('A'):
        a_nodes.append(x)

AtoZ = [] #Tracks each of the paths from A to Z.
for node in a_nodes:
    steps = 0
    current_node = node_name[node]
    while not current_node.endswith('Z'):
        index = (steps%len(directions))
        next_node = ''
        if directions[index] == 'L':
            next_node = nodes[node_name.index(current_node)][0]
        elif directions[index] == 'R':
            next_node = nodes[node_name.index(current_node)][1]
        current_node = node_name[node_name.index(next_node)]
        steps+= 1
    AtoZ.append(steps)
lcm = 1
for i in AtoZ:
    lcm = lcm*i//gcd(lcm,i)
print ("Part 2: ",lcm)