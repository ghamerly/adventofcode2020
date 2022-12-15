total = 0

def newCounter():
    return { 'count': 0 }

with open('6.in') as f:
    s = newCounter()
    for line in f:
        line = line.strip()
        if not line:
            for k in s:
                if k != 'count' and s[k] == s['count']:
                    total += 1
            s = newCounter()
        else:
            s['count'] += 1
            for c in line:
                s[c] = s.get(c, 0) + 1

    for k in s:
        if k != 'count' and s[k] == s['count']:
            total += 1

print(total)
