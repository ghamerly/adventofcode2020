

east  = lambda r, c, d, x: (r, c + x, d)
west  = lambda r, c, d, x: (r, c - x, d)
north = lambda r, c, d, x: (r - x, c, d)
south = lambda r, c, d, x: (r + x, c, d)

def forward(r, c, d, x):
    if d % 360 == 0:
        return east(r, c, d, x)
    if d % 360 == 180:
        return west(r, c, d, x)
    if d % 360 == 90:
        return north(r, c, d, x)
    if d % 360 == 270:
        return south(r, c, d, x)
    assert False

def left(r, c, d, x):
    return (r, c, d + x)

def right(r, c, d, x):
    return (r, c, d - x)

options = {
        'E': east, 'W': west, 'N': north, 'S': south,
        'L': left, 'R': right,
        'F': forward
        }

r = c = d = 0

with open('12.in') as f:
    for line in f:
        line = line.strip()
        cmd = line[0]
        x = int(line[1:])

        r, c, d = options[cmd](r, c, d, x)

        #print(line, r, c, d)

    print(abs(r) + abs(c))
