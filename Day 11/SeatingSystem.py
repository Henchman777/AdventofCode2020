'''
This code was created for Day 11 of Advent of Code.
This code finds the stable point of an airport lounge given two sets of
observations
'''
import copy

# Load seats from file
def load_seats():
    seats = []
    with open('11.txt') as file:
        for line in file:
            seats.append(list(line.rstrip('\n')))
    return seats

# Returns the number of occupied seats in the radius around a chair
def occupied_seats(seats, x, y):
    counter = 0
    for i in range(-1, 2):
        if x + i < 0 or x + i > len(seats[0]) - 1:
            continue

        for j in range(-1, 2):
            if y + j < 0 or y + j > len(seats) - 1:
                continue
            if i == 0 and j == 0:
                continue

            if seats[x+i][y+j] == '#':
                counter += 1
    return counter

# Finds the number of seats given observation 1
def find_stable_1(seats):
    update = copy.deepcopy(seats)
    old = copy.deepcopy(seats)
    old[1][0] = '#'
    while update != old:
        old = copy.deepcopy(update)
        for i, row in enumerate(old):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                elif col == 'L':
                    if occupied_seats(old, i, j) == 0:
                        update[i][j] = '#'
                elif col == '#':
                    if occupied_seats(old, i, j) >= 4:
                        update[i][j] = 'L'

    counter = 0
    for row in update:
        for col in row:
            if col == '#':
                counter += 1
    print('The number of seats that end up occupied are {}'.format(counter))
    return counter

# Finds the number of occupied chairs that a chair can see
def vis_method(seats, x, y):
    counter = 0
    directions = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))

    for i, j in directions:
        steps = 1
        while True:
            if x + i * steps < 0 or x + i * steps > len(seats[0]) - 1:
                break
            if y + j * steps < 0 or y + j * steps > len(seats) - 1:
                break
            if seats[x+i*steps][y+j*steps] == '#':
                counter += 1
                break
            elif seats[x+i*steps][y+j*steps] == 'L':
                break
            elif seats[x+i*steps][y+j*steps] == '.':
                steps += 1
    return counter

# Finds the number of occupied chairs given the second observation
def find_stable_2(seats):
    update = copy.deepcopy(seats)
    old = copy.deepcopy(seats)
    old[1][0] = '#'
    while update != old:
        old = copy.deepcopy(update)
        for i, row in enumerate(old):
            for j, col in enumerate(row):
                if col == '.':
                    continue
                elif col == 'L':
                    if vis_method(old, i, j) == 0:
                        update[i][j] = '#'
                elif col == '#':
                    if vis_method(old, i, j) >= 5:
                        update[i][j] = 'L'

    counter = 0
    for row in update:
        for col in row:
            if col == '#':
                counter += 1
    print('The number of seats that end up occupied with the new method is {}'.format(counter))
    return counter

# Main function
def main():
    seats = load_seats()
    occ_seats_1 = find_stable_1(seats)
    occ_seats_2 = find_stable_2(seats)

if __name__ == '__main__':
    main()