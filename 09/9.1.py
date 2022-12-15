with open('9.in') as f:
    x = list(map(int, f))

window = x[:25]

for i in range(26, len(x)):
    found = False
    #print(i, x[i], window)

    for j in range(25):
        for k in range(j+1, 25):
            found = window[j] + window[k] == x[i]
            if found:
                break
        if found:
            break

    if not found:
        print(x[i])

    window = window[1:] + [x[i]]
        
