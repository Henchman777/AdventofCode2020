'''
This code takes a text file and finds two numbers that add to 2020.
Once it finds those numbers, it multiplies them together to get the answer
for day 1 of advent of code
'''
TARGET_NUMBER = 2020


def open_numbers():
    # Open file. May need to change this later to specify file as input
    with open("1.txt") as file:
        numbers = []
        for line in file:
            numbers.append(int(line))
        file.close()
    return numbers


def find_2_numbers(numbers):
    # Loop through all numbers in the list and check each one
    for num in numbers:
        for second_num in numbers:
            if (num + second_num == TARGET_NUMBER):
                total = num * second_num
                print('2 Numbers: {0} + {1} = {2}'.format(num, second_num, total))
                return

def find_3_numbers(numbers):
    l = len(numbers)  
    for i in range(0, l):   
        for j in range(i, l):  
            for k in range(j, l):  
                if ((2020 - numbers[i] - numbers[j]) == numbers[k]) :   
                    total = numbers[i] * numbers[j] * numbers[k]  
                    print("3 Numbers: {0} + {1} + {2} = {3}".format(numbers[i],
                        numbers[j], numbers[k], total))
                    return

def main():
    numbers = open_numbers()
    find_2_numbers(numbers)
    find_3_numbers(numbers)

if __name__ == '__main__':
    main()
