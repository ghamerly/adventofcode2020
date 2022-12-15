with open('13.in') as f:
    earliest = int(f.readline())
    intervals = f.readline().strip().split(',')
    
intervals = [int(i) for i in intervals if i != 'x']
print(intervals)

best = []
for i in intervals:
    cycles = earliest // i
    if i * cycles == earliest:
        best.append((earliest, i))
    else:
        best.append((i * (cycles + 1), i))

best_time, best_id = min(best)
print((best_time - earliest) * best_id)
