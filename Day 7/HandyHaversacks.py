'''
This code was created for Day 7 of Advent of Code.
This code counts the number of bags that contain a certain bag and also counts
the number of bags that are contained in that certain bag.
'''
BAG_COL = 'shiny gold'
bag_found = False

# Load rules into program
def load_rules():
    rules = {}
    with open('7.txt') as file:
        for line in file:
            split_line = line.split(' ')
            base_value = split_line[0] + ' ' + split_line[1]
            if len(split_line) % 4 != 0:
                rules[base_value] = None
                continue
            rules[base_value] = {}
            for i in range(1, int(len(split_line)/4)):
                rules[base_value][split_line[i*4+1] + ' ' + split_line[i*4+2]] = split_line[i*4]

    return rules

# Recursive function that finds if the bag is in another bag
def find_bag_col(rules, curr_bag_col):
    global bag_found
    for rule in rules[curr_bag_col]:
        if rules[rule] == None:
            continue
        if rule == BAG_COL:
            bag_found = True
        find_bag_col(rules, rule)

# Find the number of bags that contain a certain bag
def bags_contain_bag(rules):
    num_bags = 0
    for rule in rules:
        global bag_found
        bag_found = False
        if rules[rule] == None:
            continue
        find_bag_col(rules, rule)
        if bag_found:
            num_bags += 1
    print('The number of bags that contain "' + BAG_COL + '" is {}'.format(num_bags))

# Recursive function that counts the number of bags contained in a bag, given a
# certain bag.
def count_bags(rules, curr_rule):
    total = 0
    for rule in rules[curr_rule]:
        total += int(rules[curr_rule][rule])
        if rules[rule] == None:
            continue
        total += int(rules[curr_rule][rule]) * count_bags(rules, rule)
    return total

# Counts the number of bags in a bag
def num_total_bags(rules):
    total = count_bags(rules, BAG_COL)
    print('A {0} bag must contain {1} other bags'.format(BAG_COL, total))

# Main function
def main():
    rules = load_rules()
    bags_contain_bag(rules)
    num_total_bags(rules)

if __name__ == '__main__':
    main()