'''
This code was written for Day 10 of Advent of Code
This code works out the number of 1-jolt differences and 3-jolt differences
as well as the number of distinct arrangements of adaptors.
'''
from collections import defaultdict

# Load adaptors sorted
def load_adaptors():
    adap = []
    adap.append(0)
    with open('10.txt') as file:
        for line in file:
            adap.append(int(line))

    adap.sort()
    return adap

# Find the number of 3 jump and 1 jumps between adaptors
def find_num_differences(adap):
    diff = {1: 0, 2: 0, 3: 0}
    prev = 0
    pos = 1
    counter = 1

    while True:
        if pos >= len(adap):
            diff[3] += 1
            break

        if adap[pos] - prev == 1:
            prev = adap[pos]
            diff[1] += 1
            pos += 1
        elif adap[pos] - prev == 2:
            prev = adap[pos]
            diff[2] += 1
            pos += 1
        elif adap[pos] - prev == 3:
            prev = adap[pos]
            diff[3] += 1
            pos += 1
        else:
            diff[3] += 1
            break
    return diff

# Find the number of distinct arrangements
def find_distinct_arrangements(adap):

    # paths[n] is the total paths from 0 to n
    paths = defaultdict(int)
    paths[0] = 1

    for adapter in adap:
        print(adapter)
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in adap:
                paths[next_adapter] += paths[adapter]
                print(paths)
                
    print('The numbr of distinct arrangements of adaptors is {}'.format(paths[max(adap)]))

# Main function
def main():
    adap = load_adaptors()
    diff = find_num_differences(adap)

    print('The number of 1-jolt differences multiplied by the 3-jolt differences is {}'.format(diff[1] * diff[3]))

    find_distinct_arrangements(adap)

if __name__ == '__main__':
    main()