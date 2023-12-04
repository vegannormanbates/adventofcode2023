#!/usr/bin/python
#Advent of Code 2023 Day 4

points = 0
cards = []
with open("input", "r") as input:
    for line in input:
        line = line.strip()
        line = (line.split(':'))[1]
        winning_numbers = (line.split('|')[0]).split()
        numbers = (line.split('|')[1]).split()
        winning_count = len(set(winning_numbers) & set(numbers))
        if winning_count == 0:
            points += 0   
        elif winning_count == 1:
            points += 1
        elif winning_count > 1:
            points += pow(2, (winning_count-1))
        cards.append([winning_numbers, numbers])
        #originally I was using a dict to record all sorts of stuff i thought would be useful - but it just made part2 impossible.
        #when trying to copy the dict into the list I kept getting type errors.
print ("Part 1: ", points)

#part 2
for index, card in enumerate(cards):
    copies = len(set(card[0]) & set(card[1]))
    for copy in range(copies):
        cards[index + 1 + copy] += cards[index]
total_cards = 0
for card in cards:
    total_cards += len(card)
total_cards = total_cards/2 #divide by two because I'm a goober and am copying both winning & my numbers into the list
print("Part 2: ", total_cards)