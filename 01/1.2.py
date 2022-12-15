with open('1.in') as f:
    v = list(map(int, f))

v.sort()

done = False

for i in v:
    for j in v:
        if done or i == j:
            continue

        for k in v:
            if done or i == k or j == k:
                continue

            if i + j + k == 2020:
                print(i * j * k)
                done = True

