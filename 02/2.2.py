with open('2.in') as f:

    valid = 0

    for line in f:
        a, b, c = line.split()
        first, second = map(int, a.split('-'))
        constraint = b[0]
        s = 0
        if first - 1 < len(c) and c[first-1] == constraint:
            s += 1
        if second - 1 < len(c) and c[second-1] == constraint:
            s += 1
        valid += (s == 1)

    print(valid)

