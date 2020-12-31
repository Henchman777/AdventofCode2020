'''
This file is for Day 4 of the Advent of Code.
This file takes a list of passports and determines which ones are valid
'''
import re

# Import the data into a list
def open_file():
    with open('4.txt') as file:
        counter = 0
        passports = []
        temp = []
        for line in file:
            if line == '\n':
                passports.append(temp)
                counter += 1
                temp = []
                continue
            step1 = line.rstrip('\n')
            step2 = step1.split(' ')
            temp.extend(step2)
        passports.append(temp)
    return passports

# Check that each passport contains the correct valid fields
def check_valid_fields(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    passport_fields = []

    for item in passport:
        passport_fields.append(item.split(':')[0])
    
    for field in req_fields:
        if field not in passport_fields:
            return True

    return False

# Checks for valid passports based on correct valid fields
# Returns a list of valid passports
def check_valid_passports(passports):
    num_valid = 0
    valid_passports = []

    for passport in passports:
        valid = True

        if not check_valid_fields(passport):
            valid = False
        if valid:
            num_valid += 1
            valid_passports.append(passport)
    print('Number of valid passports = {}'.format(num_valid))
    return valid_passports

# Checks the byr (Birth Year) value
def check_byr(value):
    byr = int(value)
    if byr >= 1920 and byr <= 2002:
        return True
    return False

# Checks the iyr (Issue Year) value
def check_iyr(value):
    iyr = int(value)
    if iyr >= 2010 and iyr <= 2020:
        return True
    return False

# Checks the eyr (Expiration Year) value
def check_eyr(value):
    eyr = int(value)
    if eyr >= 2020 and eyr <= 2030:
        return True
    return False

# Checks the hgt (Height) value
def check_hgt(value):
    values = re.split('(\d+)', value)
    height = int(values[1])

    if values[2] == '':
        return False

    if values[2] == 'cm':
        if height >= 150 and height <= 193:
            return True
        return False
    elif values[2] == 'in':
        if height >= 59 and height <= 76:
            return True
        return False
    return False

# Checks the hcl (Hair Colour) value
def check_hcl(value):
    default_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a',
        'b', 'c', 'd', 'e', 'f']
    if len(value) != 7:
        return False
    if value[0] != '#':
        return False
    
    for i in range(1, len(value)):
        if value[i] not in default_values:
            return False
    return True

# Checks the ecl (Eye Colour) value
def check_ecl(value):
    colours = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    
    if value in colours:
        return True
    return False

# Checks the pid (Passport ID) value
def check_pid(value):
    if value.isalpha():
        return False
    if len(value) != 9:
        return False
    return True

# This function checks passports based on a more strict function
def check_valid_passports2(passports):
    num_valid = 0
    
    for passport in passports:
        valid = []
        for item in passport:
            values = item.split(':')
            if values[0] == 'byr':
                valid.append(check_byr(values[1]))
            elif values[0] == 'iyr':
                valid.append(check_iyr(values[1]))
            elif values[0] == 'eyr':
                valid.append(check_eyr(values[1]))
            elif values[0] == 'hgt':
                valid.append(check_hgt(values[1]))
            elif values[0] == 'hcl':
                valid.append(check_hcl(values[1]))
            elif values[0] == 'ecl':
                valid.append(check_ecl(values[1]))
            elif values[0] == 'pid':
                valid.append(check_pid(values[1]))
        if all(valid):
            num_valid += 1
            valid = []
    
    print('Number of valid passwords after validation: {}'.format(num_valid))
    return 

# Main function
def main():
    passports = open_file()
    valid1_passports = check_valid_passports(passports)
    check_valid_passports2(valid1_passports)

if __name__ == '__main__':
    main()