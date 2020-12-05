import os
import math


current_dir = os.path.dirname(os.path.abspath(__file__))
file_contents = open(current_dir + '/day_3_input.txt', 'r').read()
lines = file_contents.split('\n')

def count_trees(steps_to_move_right, steps_to_move_down):
    tree_count = 0
    pointer = 0

    for line_i, line in enumerate(lines):
        if line_i == 0:
            continue
        if len(line) == 0:
            break
        if (line_i) % steps_to_move_down == 1:
          #  print(line)
            continue

        pointer += steps_to_move_right
        if pointer >= len(line):
            pointer -= len(line)
        if line[pointer] == '#':
            tree_count += 1

        if 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
            if line[pointer] == '#':
                print(line, ' ---> ', line[:pointer] + 'X' + line[pointer + 1:])
            if line[pointer] != '#':
                print(line, ' ---> ', line[:pointer] + '0' + line[pointer + 1:])
    return tree_count

print('part 1: ', count_trees(3, 1))

print('part 2: ', count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))

