'''
This code was created for Advent of Code Day 15.
This code finds the 2020th number and 30000000th number in a sequence.
This is very poorly implemented as the code takes around 20 seconds to run.
'''

numbers = (5,2,8,16,18,0,1)

# Finds the number spoken at a particular turn of the game
def find_number_spoken(number):
    # spoken_number : turns spoken
    spoken = {}
    # Loop through starting numbers to add them to the starting list
    for i in range(0, len(numbers)):
        spoken[numbers[i]] = []
        spoken[numbers[i]].append(i + 1)

    prev = numbers[-1]
    # Loop through the game *number of times
    for i in range(len(numbers) + 1, number + 1):
        if len(spoken[prev]) == 1:
            prev = 0
            if prev not in spoken:
                spoken[prev] = []
            spoken[prev].append(i)
            
        else:
            value = spoken[prev][-1] - spoken[prev][-2]
            if value not in spoken:
                spoken[value] = []
                spoken[value].append(i)
            else:
                spoken[value].append(i)
            prev = value
    print('The 2020th value is {}'.format(prev))

# Main function        
def main():
    find_number_spoken(2020)
    find_number_spoken(30000000)
    

if __name__ == '__main__':
    main()