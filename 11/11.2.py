with open('11.in') as f:
    seats = []
    for line in f:
        seats.append(list(line.strip()))

def occupied(s, r, c):
    o = 0

    n = len(s)
    m = len(s[0])

    inrange = lambda i, j: 0 <= i < n and 0 <= j < m

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            ri, cj = r + i, c + j
            while inrange(ri, cj) and s[ri][cj] == '.':
                ri += i
                cj += j

            if inrange(ri, cj):
                o += (s[ri][cj] == '#')

    return o

old_seats = [s[:] for s in seats]
i = 0
while i == 0 or old_seats != seats:
    i += 1
    print(i)
    for r in range(len(seats)):
        for c in range(len(seats[r])):
            if old_seats[r][c] != '.':
                o = occupied(old_seats, r, c)
                #print(r, c, old_seats[r][c], o)
                if old_seats[r][c] == 'L':
                    seats[r][c] = '#' if o == 0 else 'L'
                else:
                    seats[r][c] = 'L' if o >= 5 else '#'

    old_seats, seats = seats, old_seats
    print('\n'.join([''.join(si) for si in seats]))
    print()

o = 0
for r in seats:
    for c in r:
        if c == '#':
            o += 1
print(o)
