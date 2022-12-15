x = [0,12,6,13,20,1,17]
#x = [1, 2, 3]

prev = {}

s = -1
for i in range(2020):
    old_s = s

    #print(i, s, prev)

    if i < len(x):
        s = x[i]
    elif s in prev:
        s = i - prev[s]
    else:
        s = 0

    prev[old_s] = i

print(s)
