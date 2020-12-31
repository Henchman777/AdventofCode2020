'''
This code was created for Advent of Code Day 14.
This code puts values into memory given two different version of a program and
returns the sum of the values left into memory
'''
import math

# Load data into program
def load_program():
    program = []
    with open('14.txt') as file:
        for line in file:
            program.append(line.rstrip('\n'))
    
    return program

# Evaluate line of input to turn it into something usable
def evaluate_line(ins):
    value = ins.split(' ')

    if value[0] == 'mask':
        return value
    
    value2 = value[0].split('[')
    value3 = value2[1].rstrip(']')
    value4 = [value2[0], value3, '=', value[-1]]
    return value4

# Adds a binary number with the subnet mask (Part 1)
def add_bin_number(num, mask):
    output = ''
    for i in range(0, len(num)):
        if mask[i] == 'X':
            value = num[i]
        else:
            value = mask[i]
        output += str(value)
    return output

# Part 1 of the program
def find_sum_all_values(program):
    mask = ''
    mem = {}
    for ins in program:
        task = evaluate_line(ins)
        if task[0] == 'mask':
            mask = task[2]
        elif task[0] == 'mem':
            binary_num = '{:036b}'.format(int(task[3]))
            mem[task[1]] = add_bin_number(binary_num, mask)

    total = 0
    for key in mem:
        total += int(mem[key], 2)
    print('The sum of all values left in memory is {}'.format(total))
    
# Part 2 of the program
def version_2_software(program):
    mask = ''
    mem = {}
    # Evaluate each line in the list
    for ins in program:
        task = evaluate_line(ins)
        if task[0] == 'mask':
            mask = task[2]

        elif task[0] == 'mem':
            key = int(task[1])
            data = int(task[3])
            floating = []
            target = ''
            # Loop through each value in the mask and according to version 2
            # software, do something with the value.
            for x in range(36):
                next = mask[35-x]
                if next == '0':
                    next = str(key%2)
                if next == 'X':
                    floating.append(35-x)
                target = next + target
                key = key//2

            # Loop through each 'X' in the mask and change each value to 0's and 1's
            for i in range(0, int(math.pow(2, len(floating)))):
                for index in floating:
                    target = target[:index] + str(i%2) + target[index+1:]
                    i = i//2
                mem[int(target)] = data
    
    total = 0
    for key in mem:
        total += mem[key]
    print('The sum of values in memory is {}'.format(total))

# Main function
def main():
    program = load_program()
    find_sum_all_values(program)
    version_2_software(program)

if __name__ == '__main__':
    main()