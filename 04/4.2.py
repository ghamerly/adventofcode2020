import re

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def is_int(x, lo, hi):
    try:
        x = int(x)
        return lo <= x <= hi
    except:
        return False

def height(x):
    m = re.match('([0-9]+)(in|cm)$', x)
    if not m:
        return False
    h = m.group(1)
    return is_int(h, 59, 76) if m.group(2) == 'in' else is_int(h, 150, 193)

validation = {
        'byr': lambda x: len(x) == 4 and is_int(x, 1920, 2002),
        'iyr': lambda x: len(x) == 4 and is_int(x, 2010, 2020),
        'eyr': lambda x: len(x) == 4 and is_int(x, 2020, 2030),
        'hgt': height,
        'hcl': lambda x: bool(re.match('#[0-9a-f]{6}$', x)),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: len(x) == 9 and is_int(x, 0, 999999999),
        'cid': lambda x: True
        }

def newRecord():
    return { k: None for k in validation }

def isValid(r):
    c = len([v for v in r.values() if v is not None])
    valid = (c == len(r)) or (c + 1 == len(r) and r['cid'] is None)

    print(f'r = {r}, v = {valid}')

    for k, v in r.items():
        if v is not None:
            valid = valid and validation[k](v)
            print(f'{k}, {v}: {validation[k](v)} ({valid})')

    print()
    return valid

def main():
    valid = 0

    with open('4.in') as f:
        r = newRecord()
        for line in f:
            if line == '\n':
                valid += isValid(r)
                r = newRecord()

            p = line.split()
            for t in p:
                r[t[:3]] = t[4:]

    valid += isValid(r)

    print(valid)

main()
