#x = [0,12,6,13,20,1,17]
x = [0, 3, 6]

prev = {k: i for i, k in enumerate(x)}

s = 0
for i in range(len(x), 30000000): # I don't like the fact that this is 1 off
    #print(i, s, prev)
    old_s = s
    s = i - prev.get(s, i)
    prev[old_s] = i

print(s)
