with open('17.in') as f:
    initial = []
    for line in f:
        initial.append(list(line.strip()))

active = set()

for i, row in enumerate(initial):
    for j, col in enumerate(row):
        if col == '#':
            active.add((i, j, 0, 0))

def e(l, p=0, diff=False):
    if p == len(l):
        if diff:
            yield tuple(l)
    else:
        ll = list(l)
        for i in [-1, 0, 1]:
            ll[p] = l[p] + i
            yield from e(ll, p+1, diff or i != 0)

def disp(active):
    r_vals = [r for r, _, _ in active]
    c_vals = [c for _, c, _ in active]
    d_vals = [d for _, _, d in active]

    for d in range(min(d_vals), max(d_vals) + 1):
        for r in range(min(r_vals), max(r_vals) + 1):
            row = []
            for c in range(min(c_vals), max(c_vals) + 1):
                row.append('#' if (r, c, d) in active else ' ')
            print(''.join(row))

        print()

for _ in range(6):
    print('-' * 30)
    #disp(active)

    count = {}
    for r, c, d, z in active:
        for k in e([r, c, d, z]):
            count[k] = count.get(k, 0) + 1

    keys = active | count.keys()
    r_vals = [r for r, _, _, _ in keys]
    c_vals = [c for _, c, _, _ in keys]
    d_vals = [d for _, _, d, _ in keys]
    z_vals = [z for _, _, _, z in keys]

    next_active = set()
    for r in range(min(r_vals) - 1, max(r_vals) + 2):
        for c in range(min(c_vals) - 1, max(c_vals) + 2):
            for d in range(min(d_vals) - 1, max(d_vals) + 2):
                for z in range(min(z_vals) - 1, max(z_vals) + 2):
                    k = (r, c, d, z)
                    if k in active and count.get(k, 0) in (2, 3):
                        next_active.add(k)
                    elif k not in active and count.get(k, 0) == 3:
                        next_active.add(k)

    active = next_active

print(len(active))
