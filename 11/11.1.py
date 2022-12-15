with open('11.in') as f:
    seats = []
    for line in f:
        seats.append(list(line.strip()))

def occupied(s, r, c):
    o = 0
    for i in range(r-1, r+2):
        if not 0 <= i < len(s):
            continue

        for j in range(c-1, c+2):
            if (i == r and j == c) or not 0 <= j < len(s[0]):
                continue

            if s[i][j] == '#':
                o += 1

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
                    seats[r][c] = 'L' if o >= 4 else '#'

    old_seats, seats = seats, old_seats
    #print('\n'.join([''.join(si) for si in seats]))
    #print()

o = 0
for r in seats:
    for c in r:
        if c == '#':
            o += 1
print(o)
