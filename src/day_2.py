import os
import re

current_dir = os.path.dirname(os.path.abspath(__file__))
file_contents = open(current_dir + '/day_2_input.txt', 'r').read()
lines = file_contents.split('\n')

re_lines = [re.match(r'(\d+)-(\d+) (\w): (.+)', line) for line in lines if line != '']

matching_passwords = 0
matching_passwords_2 = 0
for match in re_lines:
    password = match.group(4)
    num_1 = int(match.group(1))
    num_2 = int(match.group(2))

    character_count = password.count(match.group(3))
    if character_count >= num_1 and character_count <= num_2:
        matching_passwords += 1

    if len(password) <= num_1 - 1:
        char_a = None
    else:
        char_a = password[num_1 - 1]
    if len(password) <= num_2 - 1:
        char_b = None
    else:
        char_b = password[num_2 - 1]
    is_char_a_match = char_a == match.group(3)
    is_char_b_match = char_b == match.group(3)
    print(is_char_a_match, char_a, is_char_b_match, char_b, password, match)
    if (is_char_a_match or is_char_b_match) and is_char_a_match != is_char_b_match:
        matching_passwords_2 += 1

print(f'matching passwords for part 1: {matching_passwords}')
print(f'matching passwords for part 2: {matching_passwords_2}')

