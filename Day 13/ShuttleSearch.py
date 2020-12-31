'''
This code was written for Day 13 of Advent of Code.
This code finds the earliest bus at a set time and the earlist time where all
buses come one minute after each other.
'''
from functools import reduce

# Load data from file
def load_notes():
    time = 0
    bus_ids = []
    with open('13.txt') as file:
        time = int(file.readline())
        bus_ids = file.readline().split(',')

    return time, bus_ids

# Part 1. Find earliest bus time
def find_earliest_bus(time, bus_list):
    min_time = time * time
    bus_num = 0

    for bus in bus_list:
        if bus == 'x':
            continue

        ctr = 1
        while True:
            value = int(bus) * ctr
            if value > time:
                if value < min_time:
                    bus_num = bus
                    min_time = value
                break
            ctr += 1
    wait_time = min_time - time
    total = int(bus_num) * wait_time
    print('The value for Part 1 is {}'.format(total))

# Implement chinese remainder theorem
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

# Find the multiplicative inverse. Used in the chinese remainder thm.
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Part 2. Find the time which has all subsequence busses a minute apart
def find_subs_bus(buses):
    for i in range(0, len(buses)):
        if buses[i] == 'x':
            buses[i] = 1
            continue
        buses[i] = int(buses[i])
    remainders = [int(bus) - i for i, bus in enumerate(buses)]

    output = chinese_remainder(buses, remainders)
    print('The ealiest timestamp is {}'.format(output))
 
# Main function
def main():
    time, bus_ids = load_notes()
    find_earliest_bus(time, bus_ids)
    find_subs_bus(bus_ids)

if __name__ == '__main__':
    main()