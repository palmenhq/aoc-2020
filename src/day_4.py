import os
import re


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

def is_passport_valid(passport):
    if not has_passport_all_valid_fields(passport):
        return False
    fields = get_passport_fields(passport)
    is_valid = True
    for field in fields:
        if len(field) == 0:
            continue

        [key, value] = field.split(':')
        if key == 'byr' and not (value.isdigit() and int(value) <= 2002 and int(value) >= 1920):
            return False
        if key == 'iyr' and not (value.isdigit() and int(value) <= 2020 and int(value) >= 2010):
            return False
        if key == 'eyr' and not (value.isdigit() and int(value) <= 2030 and int(value) >= 2020):
            return False
        if key == 'hgt':
            if value.endswith('in'):
                value_f = float(value.replace('in', ''))
                if value_f <= 76 and value_f >= 59:
                    continue
                else:
                    return False
            elif value.endswith('cm'):
               value_f = float(value.replace('cm', ''))
               if value_f <= 193 and value_f >= 150:
                   continue
               else: 
                   return False
            else:
                return False
        if key == 'hcl':
            if not re.match(r'#[a-f0-9]{6}', value):
                return False
        if key == 'ecl':
            if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        if key == 'pid':
            if len(value) != 9 or not value.isdigit():
                return False
        if key == 'cid':
            pass


    return True


valid_passports = [passport for passport in passports if has_passport_all_valid_fields(passport)]
print('Valid passports (part 1): ', len(valid_passports))

valid_passports_pt_2 = [passport for passport in passports if is_passport_valid(passport)]
print('Valid passports (part 2): ', len(valid_passports_pt_2))

