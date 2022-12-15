with open('3.in') as f:
    trees = list(map(str.strip, f))

slope_counts = {
        (1, 1): 0,
        (1, 3): 0,
        (1, 5): 0,
        (1, 7): 0,
        (2, 1): 0
        }

width = len(trees[0])


for rd, cd in slope_counts:
    row, col = 0, 0
    while row < len(trees):
        slope_counts[(rd, cd)] += trees[row][col % width] == '#'
        row += rd
        col += cd

ans = 1
for v in slope_counts.values():
    ans *= v
print(ans)

