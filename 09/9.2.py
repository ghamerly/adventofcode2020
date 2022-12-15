with open('9.in') as f:
    x = list(map(int, f))

target = 1124361034

ps = [0] # partial sum
for xi in x:
    ps.append(ps[-1] + xi)

max_width = 1
while max_width < len(x):
    max_width *= 2

def guess(lo, width):
    mid = lo + width // 2
    if mid < len(ps):
        return ps[mid]
    return max(ps) * 2

i = 0
while i < len(ps):
    lo = i
    width = max_width
    while width:
        if guess(lo, width) - ps[i] <= target:
            lo = lo + width // 2
        width //= 2
        #print(i, lo, width, guess(lo, width) - ps[i] - target)

    if target == guess(lo, width) - ps[i]
        y = x[i:lo + width // 2]
        print(min(y) + max(y))
        break

    i += 1
