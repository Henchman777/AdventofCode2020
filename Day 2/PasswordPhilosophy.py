'''
This code is for the second day of Advent of Code.
This code checks if a password is valid, given a specific password policy.
'''
class PasswordPolicy:
    '''
    Defines a list of what a password should contine. This includes the min
    number of times a letter appears, the max number of times a letter appears,
    the letter we need to check for and the password.
    '''
    def __init__(self, n1, n2, letter, password):
        self.n1 = n1
        self.n2 = n2
        self.letter = letter
        self.password = password

# Get the inputs and put them in a format that we can use
def get_inputs():
    password_list = []
    with open('2.txt') as file:
        for line in file:
            policy = line.split(' ')
            numbers = policy[0].split('-')
            letter = policy[1][0]
            password = policy[2][:-1]
            new_class = PasswordPolicy(numbers[0], numbers[1], letter, password)
            password_list.append(new_class)
    return password_list

# Check for valid passwords given the first part of the question
def check_passwords_valid1(passwords):
    valid_passwords = 0
    for i in passwords:
        counter = 0
        for letter in i.password:
            if letter == i.letter:
                counter += 1
        if (counter >= int(i.n1) and counter <= int(i.n2)):
            valid_passwords += 1
    print(valid_passwords)

# Check for valid passwords given the second part of the question
def check_passwords_valid2(passwords):
    valid_passwords = 0
    for i in passwords:
        n1 = int(i.n1)
        n2 = int(i.n2)

        if i.password[n1-1] == i.letter:
            if i.password[n2-1] != i.letter:
                valid_passwords += 1

        elif i.password[n2-1] == i.letter:
            valid_passwords += 1
    print(valid_passwords)
       

def main():
    passwords = get_inputs()
    check_passwords_valid1(passwords)
    check_passwords_valid2(passwords)

if __name__ == '__main__':
    main()