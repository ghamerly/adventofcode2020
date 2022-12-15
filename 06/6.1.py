total = 0

with open('6.in') as f:
    s = set()
    for line in f:
        line = line.strip()
        if not line:
            total += len(s)
            s = set()
        else:
            s |= set(line)

    total += len(s)

print(total)
