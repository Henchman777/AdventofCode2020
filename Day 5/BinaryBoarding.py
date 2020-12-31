'''
This code was written for Day 5 of Advent of code.
This code finds information about a seating plan. The max seat ID number and
the missing seat number.
'''
# Load passes from file into program. Example is FBBFFBFRLL
def load_passes():
    passes = []
    with open('5.txt') as file:
        for line in file:
            passes.append(line.rstrip('\n'))
    return passes

# Finds and returns the seat ID of a seat
def find_pass_id(seat):
    min_row = 0
    max_row = 127
    row = 0
    min_col = 0
    max_col = 7
    col = 0

    for i in range(0, 7):
        if seat[i] == 'F':
            max_row = (max_row + min_row + 1)/2 - 1
            row = max_row
        elif seat[i] == 'B':
            min_row = (max_row + min_row + 1)/2
            row = min_row
    for i in range(7, 10):
        if seat[i] == 'L':
            max_col = (max_col + min_col + 1)/2 - 1
            col = max_col
        elif seat[i] == 'R':
            min_col = (max_col + min_col + 1)/2
            col = min_col

    return row * 8 + col

# Returns the highest seat number
def find_highest_pass(passes):
    highest_id = 0
    for seat in passes:
        seat_id = find_pass_id(seat)
        if seat_id > highest_id:
            highest_id = seat_id

    print('Highest seat ID is {}'.format(highest_id))
    return highest_id

# Returns the lowest seat number
def find_lowest_pass(passes):
    lowest_id = 800
    for seat in passes:
        seat_id = find_pass_id(seat)
        if seat_id < lowest_id:
            lowest_id = seat_id
    return lowest_id

# Finds the missing seat number
def find_missing_pass(passes):
    seat_num = 0

    seat_ids = []
    for i in range(0, len(passes)):
        seat_ids.append(find_pass_id(passes[i]))
    seat_ids.sort()
    
    for i in range(0, len(passes)):
        if seat_ids[i+1] - seat_ids[i] > 1:
            seat_num = seat_ids[i] + 1
            break
    print('Missing seat is at seat ID {}'.format(seat_num))

# Main program
def main():
    passes = load_passes()
    find_highest_pass(passes)
    find_missing_pass(passes)

if __name__ == '__main__':
    main()