'''
This code was created for Day 16 of Advent Of Code.
This code finds the numbers in tickets that are invalid before removing them and
finally locating which numbers on your ticket are ones starting with the word
departure.
'''
import copy

# Initialise global variables
rules = {}
my_ticket = []
near_tickets = []

# Process the rules to split values
def process_rules(load_rules):
    for i in range(0, len(load_rules)):
        split = load_rules[i].split(': ')
        split2 = split[1].split(' or ')
        rules[split[0]] = split2

# Load the notes from the text file into the memory
def load_notes():
    load_rules = []
    with open('16.txt', 'r') as file:
        for line in file:
            if line == '\n':
                break
            load_rules.append(line.rstrip('\n'))
        
        for line in file:
            if line == '\n':
                break
            my_ticket.append(line.rstrip('\n').split(','))

        for line in file:
            if line == '\n':
                break
            near_tickets.append(line.rstrip('\n').split(','))

    process_rules(load_rules)

# Check to see if a number is in the rules
def check_valid_number(num):
    valid = False
    for rule in rules:
        values1 = rules[rule][0].split('-')
        values2 = rules[rule][1].split('-')

        if num >= int(values1[0]) and num <= int(values1[1]):
            valid = True
        
        if num >= int(values2[0]) and num <= int(values2[1]):
            valid = True
    return valid

# Find the error rate of the numbers
def find_error_rate():
    not_valid_numbers = []
    not_valid_tickets = []
    for i in range(1, len(near_tickets)):
        for j in range(0, len(near_tickets[i])):
            if not check_valid_number(int(near_tickets[i][j])):
               not_valid_numbers.append(int(near_tickets[i][j]))
               not_valid_tickets.append(i)
    
    total = 0
    for num in not_valid_numbers:
        total += num
    #print(total)
    return not_valid_tickets

# Remove the invalid tickets from the global variables given the ticket numbers
def take_out_invalid_tickets(not_valid_tickets):
    global near_tickets
    temp = []
    temp.append(near_tickets[0])
    for i in range(1, len(near_tickets)):
        if i in not_valid_tickets:
            continue
        temp.append(near_tickets[i])
    near_tickets = temp

# Find the fields that a paritcular row could be apart of
def find_field(fields, map, list):
   # print(list)
    not_possible = set()
    for rule in fields:
        #print(rule)
        
        values1 = rules[rule][0].split('-')
        values2 = rules[rule][1].split('-')

        for num in list:
            if int(num) >= int(values1[0]) and int(num) <= int(values1[1]):
                continue
            elif int(num) >= int(values2[0]) and int(num) <= int(values2[1]):
                continue
            else:
                not_possible.add(rule)
    
    #print(not_possible)
    return fields - not_possible

# Find which fields belong to which rows
def locate_fields():
    map = {}
    fields = set(rules.keys())
    rows = tuple(zip(*near_tickets[1:]))

    do = {i for i in range(0, len(rows))}
    while do != set():
        value = do.pop()
        field = find_field(fields, map, rows[value])
        if len(field) > 1:
            do.add(value)
            continue
        map[list(field)[0]] = value
        fields = fields - field
    
    locations = []
    for item in map:
        if 'departure' in item:
            locations.append(map[item])
            print(item, map[item])

    total = 1
    print(my_ticket)
    for num in locations:
        print(num)
        total *= int(my_ticket[1][num])
    print(total)

# Main program
def main():
    load_notes()
    not_valid_tickets = find_error_rate()
    take_out_invalid_tickets(not_valid_tickets)
    locate_fields()


if __name__ == '__main__':
    main()