'''
This code was written for Day 12 of Advent of Code.
This code reads a set of instructions and fins the manhatten distance from the
start point to the end point after the instructions have been actioned.
There are two different rules given the same set of instructions
'''
import math

# Load directions
def load_dir():
    directions = []
    with open('12.txt') as file:
        for line in file:
            directions.append(line.rstrip('\n'))
    return directions

# Change ships direction
def change_direction(item, facing):
    map = ['N', 'E', 'S', 'W']
    map2 = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    turning = 1
    if item[0] == 'L':
        turning = -1
    value = int(int(item[1:])/90) * turning
    turn = (map2[facing] + value) % 4
    return map[turn]

# Find the distsance given the first set of rules
def find_distance(directions):
    facing = 'E'
    dist = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
    for item in directions:
        if item[0] == 'F':
            dist[facing] += int(item[1:])
        elif item[0] == 'N':
            dist['N'] += int(item[1:])
        elif item[0] == 'E':
            dist['E'] += int(item[1:])
        elif item[0] == 'S':
            dist['S'] += int(item[1:])
        elif item[0] == 'W':
            dist['W'] += int(item[1:])
        elif item[0] == 'R' or item[0] == 'L':
            facing = change_direction(item, facing)

    total = abs(abs(dist['E']) - abs(dist['W'])) + abs(abs(dist['N']) - abs(dist['S']))
    print('Manhattan distance between start and now is {}'.format(total))

# Move the ship towards the waypoint
def move_ship(waypoint, value, dist):
    dist['N'] += waypoint[0] * value
    dist['E'] += waypoint[1] * value
    dist['S'] += waypoint[2] * value
    dist['W'] += waypoint[3] * value

# Rotate the waypoint around the values
def rotate_waypoint(waypoint, item, map):
    turning = 1
    if item[0] == 'L':
        turning = -1

    value = int(int(item[1:])/90) * turning
    turn = value % 4
    
    temp = waypoint.copy()
    for i in range(0, len(waypoint)):
        waypoint[(i+turn) % 4] = temp[i]

# Find the distance with the waypoint as directions
def find_waypoint_dist(directions):
    map = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    dist = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    # North | East | South | West
    waypoint = [1, 10, 0, 0]
    for item in directions:
        if item[0] == 'F':
            move_ship(waypoint, int(item[1:]), dist)
        elif item[0] == 'N':
            waypoint[map['N']] += int(item[1:])
        elif item[0] == 'E':
            waypoint[map['E']] += int(item[1:])
        elif item[0] == 'S':
            waypoint[map['S']] += int(item[1:])
        elif item[0] == 'W':
            waypoint[map['W']] += int(item[1:])
        elif item[0] == 'R' or item[0] == 'L':
            rotate_waypoint(waypoint, item, map)

    total = abs(abs(dist['E']) - abs(dist['W'])) + abs(abs(dist['N']) - abs(dist['S']))
    print('Manhattan distance between start and now is {}'.format(total))

# Main function
def main():
    directions = load_dir()
    find_distance(directions)
    find_waypoint_dist(directions)

if __name__ == '__main__':
    main()