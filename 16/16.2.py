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

    possible_fields = { k: set(range(len(fields))) for k in fields }

    for line in f:
        t = list(map(int, line.strip().split(',')))
        assert len(t) == len(fields)
        
        valid = True
        for v in t:
            for (r1_lo, r1_hi), (r2_lo, r2_hi) in fields.values():
                if r1_lo <= v <= r1_hi or r2_lo <= v <= r2_hi:
                    break
            else:
                valid = False

        if valid:
            for i, v in enumerate(t):
                for k, ((r1_lo, r1_hi), (r2_lo, r2_hi)) in fields.items():
                    if not (r1_lo <= v <= r1_hi or r2_lo <= v <= r2_hi):
                        possible_fields[k].remove(i)

    assigned_fields = {}

    # there has got to be a more elegant general purpose algorithm than this;
    # something based on maximum matching?
    while len(assigned_fields) < len(fields):
        for k, v in possible_fields.items():
            if len(v) == 1:
                v = next(iter(v))
                assigned_fields[k] = v
                possible_fields[k] = []

                for k2, v2 in possible_fields.items():
                    if v in v2:
                        v2.remove(v)

    for f in possible_fields:
        print(f, possible_fields[f])

    print()

    ans = 1
    for f in assigned_fields:
        if f.startswith('departure'):
            print(my_ticket, assigned_fields[f], my_ticket[assigned_fields[f]])
            ans *= my_ticket[assigned_fields[f]]
        print(f, assigned_fields[f])

    print(ans)
