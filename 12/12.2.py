class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def east(self, x): self.x += x
    def west(self, x): self.x -= x
    def north(self, x): self.y += x
    def south(self, x): self.y -= x

    def forward(self, x, other):
        self.x += x * other.x
        self.y += x * other.y

    def left(self, x):
        #print('left', self, x, around)
        if x % 360 == 0:
            return

        old_x = self.x
        old_y = self.y

        if x % 360 == 90:
            self.x = -old_y
            self.y = old_x
        elif x % 360 == 180:
            self.x = -old_x
            self.y = -old_y
        elif x % 360 == 270:
            self.x = old_y
            self.y = -old_x
        else:
            assert False

    def right(self, x):
        self.left(-x)

    def decode(self, cmd, x):
        options = {
                'E': self.east,
                'W': self.west,
                'N': self.north,
                'S': self.south
                }

        options[cmd](x)

    def __repr__(self):
        return f'{self.x} {self.y}'

ship = Point(0, 0)
waypoint = Point(10, 1)
print(f'{ship} {waypoint}')

with open('12.in') as f:
    for line in f:
        line = line.strip()
        cmd = line[0]
        x = int(line[1:])

        if cmd in 'EWNS':
            waypoint.decode(cmd, x)
        elif cmd == 'L':
            waypoint.left(x)
        elif cmd == 'R':
            waypoint.right(x)
        elif cmd == 'F':
            ship.forward(x, waypoint)

        print(f'{line}: {ship} {waypoint}')

    print(abs(ship.x) + abs(ship.y))
