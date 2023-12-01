#!/usr/bin/python
#Advent of Code 2023 Day 1

#Part 1

line_numbers = []
#For part 2:
translate_dict = {
    'one':  'o1e',
    'two':  't2o',
    'three':    't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six':  's6x',
    'seven':    's7n',
    'eight':    'e8t',
    'nine': 'n9e'
}
#Iterating through the dictionary doesn't work because it replaces letters that might otherwise spell out different numbers
#I guess just putting border letters in the string is a hacky work around? Tried sorting but that didn't really fix the problem of
#replacing shared letters

with open("input", "r") as input:
    for line in input:
        for number in translate_dict:
            line = line.replace(number,translate_dict[number])

        for char in line:
            if char.isdigit():
                first_digit = char
                break
        for char in line[::-1]:
            if char.isdigit():
                second_digit = char
                break
        number = int(first_digit + second_digit)
        line_numbers.append(number)
print(sum(line_numbers))