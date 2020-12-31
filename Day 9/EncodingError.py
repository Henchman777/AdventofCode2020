'''
This code was created for Day 9 of Advent of Code.
This code finds a number in a preamble of numbers that does not follow a
a specific property. Then, the code will find numbers in the set that add
to the number that doesn't follow the specific property.
'''
# Change this value to the size of the preamble
PREAMBLE = 25

# Load data from file
def load_xmas():
    xmas = []
    with open('9.txt') as file:
        for line in file:
            xmas.append(int(line.rstrip('\n')))
    return xmas

# Check the preamble to see if the property is satisfied
def check_property(preamble, value):
    for i in range(0, len(preamble)):
        for j in range(0, len(preamble)):
            if preamble[i] == preamble[j]:
                continue
            if preamble[i] + preamble[j] == value:
                return True
    return False

# Find the first number where the property doesn't occur
def find_first_non_sum(xmas):
    value = 0
    for i in range(PREAMBLE, len(xmas)):
        if not check_property(xmas[i-PREAMBLE:i], xmas[i]):
            value = xmas[i]
            break
    print('First number that does not have the property is {}'.format(value))
    return value

# Find the set of numbers that add to the invalid number
def find_cont_set(xmas, inv_num):
    set = []
    for i in range(0, len(xmas)):
        set.append(xmas[i])
        set.append(xmas[i+1])
        total = 0
        counter = i+2
        while True:
            for val in set:
                total += val
            if total > inv_num:
                set = []
                break
            elif total < inv_num:
                set.append(xmas[counter])
                counter += 1
                total = 0
            else:
                return set
    return set

# Find the encryption weakness value
def find_enc_weakness(xmas, inv_num):
    contigous_set = find_cont_set(xmas, inv_num)
    contigous_set.sort()
    weakness = contigous_set[0] + contigous_set[-1]
    print('The encryption weakness is {}'.format(weakness))

# Main function
def main():
    xmas = load_xmas()
    inv_num = find_first_non_sum(xmas)
    find_enc_weakness(xmas, inv_num)

if __name__ == '__main__':
    main()