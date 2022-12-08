import re

with open('test/puzzle_input.txt') as f:
    passport_strings = f.read().split("\n\n")
    passport_strings = [x.replace('\n', ' ') for x in passport_strings]


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid' is not required

valid_passports = []
passports = []
for passport_string in passport_strings:
    passport = {}
    for entry in passport_string.split():
        field, value = entry.split(':')
        passport[field] = value
    passports.append(passport)

for passport in passports:
    if not (set(required_fields) - passport.keys()):
        valid_passports.append(passport)

print("Part 1:", len(valid_passports))  # PART 1: 250


# Part 2:
count = 0
for valid_passport in valid_passports:
    if not 1920 <= int(valid_passport['byr']) <= 2002:  # Correct
        continue
    if not 2010 <= int(valid_passport['iyr']) <= 2020:  # Correct
        continue
    if not 2020 <= int(valid_passport['eyr']) <= 2030:  # Correct
        continue
    if not (valid_passport['hgt'].endswith('cm') or valid_passport['hgt'].endswith('in')):  # correct
        continue
    if valid_passport['hgt'].endswith('cm'):
        if not 150 <= int(valid_passport['hgt'].rstrip('cm')) <= 193:
            continue
    else:
        if not 59 <= int(valid_passport['hgt'].rstrip('in')) <= 76:
            continue
    if not re.fullmatch(r"#[a-f, 0-9]{6}", valid_passport['hcl']):
        continue
    if valid_passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        continue
    if not re.fullmatch(r"[0-9]{9}", valid_passport['pid']):
        continue

    count += 1

print("Part 2:", count)
# Part 2: 158 is correct
