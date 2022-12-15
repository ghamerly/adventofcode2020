def parse(line):
    k, v = line.split(': ')
    range1, range2 = v.split(' or ')
    range1 = list(map(int, range1.split('-')))
    range2 = list(map(int, range2.split('-')))

    return k, (range1, range2)

with open('16.in') as f:
    fields = {}
    for line in f:
        line = line.strip()
        if not line:
            break
        key, ranges = parse(line)

        fields[key] = ranges

    print(fields)

    assert next(f) == 'your ticket:\n'
    my_ticket = list(map(int, next(f).strip().split(',')))
    print(my_ticket)
    assert len(my_ticket) == len(fields)

    assert next(f) == '\n'
    assert next(f) == 'nearby tickets:\n'

    tally = 0
    for line in f:
        t = list(map(int, line.strip().split(',')))
        assert len(t) == len(fields)
        
        for v in t:
            for (r1_lo, r1_hi), (r2_lo, r2_hi) in fields.values():
                if r1_lo <= v <= r1_hi or r2_lo <= v <= r2_hi:
                    break
            else:
                tally += v
                print('invalid:', v)

    print(tally)
