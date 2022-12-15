with open('2.in') as f:

    valid = 0

    for line in f:
        a, b, c = line.split()
        low, high = map(int, a.split('-'))
        constraint = b[0]
        count = c.count(constraint)
        if low <= count <= high:
            valid += 1

    print(valid)

