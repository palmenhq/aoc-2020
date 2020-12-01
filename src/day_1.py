import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file_contents = open(current_dir + '/day_1_input.txt', 'r').read()
string_numbers = file_contents.split('\n')
numbers = [int(string_number) for string_number in string_numbers if string_number != '']

for n in numbers:
    if 2020 - n in numbers:
        print(f"found the number! It's {(2020 - n) * n}")
        break

for n0 in numbers:
    for n1 in numbers:
        expected_number = 2020 - (n0 + n1)
        if expected_number in numbers:
            print(f"found the number for part 2! It's {expected_number * n0 * n1}")
            exit(0)


