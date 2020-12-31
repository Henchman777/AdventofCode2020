'''
This code was created for Day 8 of Advent of Code.
This program calculates the accumulator value just before an infinite loop
occurs and then when the program is fixed and exits.
'''
# Initialise global accumulator value
acc = 0

# Load code into program
def load_code():
    code = []
    with open('8.txt') as file:
        for line in file:
            code.append(line.rstrip('\n'))
    return code

# Handle acc instruction
def handle_acc(value):
    operand = value[0]
    num = int(value[1:])
    global acc

    if operand == '+':
        acc += num
    elif operand == '-':
        acc -= num

# Find the value of acc before there occurs an infinite loop
def find_acc_before_loop(code):
    pointer = 0
    visited = []

    while True:
        if pointer in visited:
            break
        visited.append(pointer)

        ins = code[pointer].split(' ')
        if ins[0] == 'acc':
            handle_acc(ins[1])
            pointer += 1

        elif ins[0] == 'nop':
            pointer += 1

        elif ins[0] == 'jmp':
            if ins[1][0] == '+':
                pointer += int(ins[1][1:])
            elif ins[1][0] == '-':
                pointer -= int(ins[1][1:])
    global acc
    print('Accumulator value before loop is {}'.format(acc))

# Check to see if an infinite loop occurs
def check_loop(code):
    global acc
    acc = 0
    pointer = 0
    visited = []

    while True:
        if pointer >= len(code):
            break
        if pointer in visited:
            return True
        visited.append(pointer)

        ins = code[pointer].split(' ')
        if ins[0] == 'acc':
            handle_acc(ins[1])
            pointer += 1

        elif ins[0] == 'nop':
            pointer += 1

        elif ins[0] == 'jmp':
            if ins[1][0] == '+':
                pointer += int(ins[1][1:])
            elif ins[1][0] == '-':
                pointer -= int(ins[1][1:])

    return False

# Try and fix the code by changine nop -> jmp and jmp -> nop one at a time.
def fix_code(code):
    for i in range(7, len(code)):
        copy_code = code.copy()
        if code[i].split(' ')[0] == 'acc':
            continue
        elif code[i].split(' ')[0] == 'nop':
            copy_code[i] = 'jmp ' + code[i].split(' ')[1]

        elif code[i].split(' ')[0] == 'jmp':
            copy_code[i] = 'nop ' + code[i].split(' ')[1]
        if not check_loop(copy_code):
            break

    print('Acc value after termination is {}'.format(acc))

# Main function
def main():
    code = load_code()
    find_acc_before_loop(code)
    fix_code(code)

if __name__ == '__main__':
    main()