'''
This is code written for the third day of Advent of Code
This code counts the number of 'trees' (#) in a map of trees.
This does so given the slope of how we count the trees
'''
def get_input():
    trees = []
    with open('3.txt') as file:
        for line in file:
            trees.append(line[:-1])
    return trees

# Count the number of trees in a slope given the slop
def count_num_trees(trees, right, down):
    right_ind = 0
    down_ind = 0
    counter = 0
    height = len(trees)
    
    while True:
        right_ind += right
        down_ind += down

        if down_ind >= height:
            break
        if right_ind > len(trees[down_ind]) - 1:
            right_ind = right_ind - len(trees[down_ind])
        
        if trees[down_ind][right_ind] == '#':
            counter += 1
    print('Number of trees is {}'.format(counter))
    return counter

# Multiple the number of trees together given a list of slopes
def count_num_trees_mul_slopes(trees):
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    multiplyer = 1
    for i in slopes:
        multiplyer = multiplyer * count_num_trees(trees, i[0], i[1])
    
    print('The multiplyer is {}'.format(multiplyer))

def main():
    trees = get_input()
    count_num_trees(trees, 3, 1)

    count_num_trees_mul_slopes(trees)

if __name__ == '__main__':
    main()