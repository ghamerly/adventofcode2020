with open('10.in') as f:
    x = list(map(int, f))

x.sort()
x = [0] + x

diffs = { 0: 0, 1: 0, 2: 0, 3: 0 }
for i in range(1, len(x)):
    d = x[i] - x[i-1]
    diffs[d] += 1
diffs[3] += 1

print(diffs[1] * diffs[3])
