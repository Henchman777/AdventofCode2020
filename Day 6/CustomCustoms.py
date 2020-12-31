'''
This code was created for Day 6 of Advent of Code.
This code finds the sum of answers that anyone answered and everyone answered.
'''
# Load input
def load_answers():
    with open('6.txt') as file:
        counter = 0
        answers = []
        temp = []
        for line in file:
            if line == '\n':
                answers.append(temp)
                counter += 1
                temp = []
                continue
            step1 = line.rstrip('\n')
            step2 = step1.split(' ')
            temp.extend(step2)
        answers.append(temp)
    return answers

# Find questions that anyone answered
def find_questions_anyone_answered(answers):
    total = 0
    for group in answers:
        answered_questions = []
        for person in group:
            for i in range(0, len(person)):
                if person[i] not in answered_questions:
                    answered_questions.append(person[i])
        total += len(answered_questions)
    print('Sum of questions anyone answered in a group is {}'.format(total))

# Find questions that everyone answered
def find_questions_everyone_answered(answers):
    total = 0
    for group in answers:
        answered_questions = []
        same_answers = []
        
        for i in group[0]:
            answered_questions.append(i)
            same_answers.append(i)
        
        for person in group:
            if person == group[0]:
                continue
            for i in answered_questions:
                print(i)
                if i not in person:
                    same_answers.remove(i)
            answered_questions = same_answers.copy()
        total += len(answered_questions)
    print('Sum of questions everyone answered in a group is {}'.format(total))

# Main function
def main():
    answers = load_answers()
    find_questions_anyone_answered(answers)
    find_questions_everyone_answered(answers)

if __name__ == '__main__':
    main()