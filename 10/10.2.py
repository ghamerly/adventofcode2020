with open('10.in') as f:
    x = list(map(int, f))

x.sort()
x = [0] + x + [max(x) + 3]

n = [0] * len(x)
n[0] = 1

for j in range(1, len(x)):
    i = j - 1
    while i >= 0 and x[i] + 3 >= x[j]:
        n[j] += n[i]
        i -= 1

print(n[-1])
