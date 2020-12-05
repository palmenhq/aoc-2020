import os


current_dir = os.path.dirname(os.path.abspath(__file__))
file_contents = open(current_dir + '/day_4_input.txt', 'r').read()

passports = file_contents.split('\n\n')

def get_passport_fields(passport_string):
    lines = passport_string.split('\n')
    fields = [field for fields in [line.split(' ') for line in lines] for field in fields]
    return fields

REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def has_passport_all_valid_fields(passport):
    fields = get_passport_fields(passport)
    field_keys = [field.split(':')[0] for field in fields]

    is_valid = True
    for required_key in REQUIRED_KEYS:
        is_valid = is_valid and required_key in field_keys

    return is_valid

n_valid_passports = 0
for passport in passports:
    if has_passport_all_valid_fields(passport):
        n_valid_passports += 1

print('Valid passports (part 1): ', n_valid_passports)



