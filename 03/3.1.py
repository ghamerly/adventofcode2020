with open('3.in') as f:
    trees = list(map(str.strip, f))

width = len(trees[0])

row = col = 0
count = 0

while row < len(trees):
    count += trees[row][col % width] == '#'
    row += 1
    col += 3

print(count)

