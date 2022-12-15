
def newRecord():
    return { 'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None,
            'ecl': None, 'pid': None, 'cid': None }

valid = 0

def isValid(r):
    c = len([v for v in r.values() if v is not None])
    return (c == len(r)) or (c + 1 == len(r) and r['cid'] is None)

with open('4.in') as f:
    r = newRecord()
    for line in f:
        if line == '\n':
            valid += isValid(r)
            r = newRecord()

        p = line.split()
        for t in p:
            r[t[:3]] = 1

valid += isValid(r)

print(valid)
