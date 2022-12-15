with open('1.in') as f:
    v = list(map(int, f))

v.sort()

i = 0
j = len(v) - 1

while i < j and v[i] + v[j] != 2020:
    if v[i] + v[j] < 2020:
        i += 1
    else:
        j -= 1

print(v[i], v[j], v[i] * v[j])
