seat_ids = []

with open('5.in') as f:
    for line in f:
        row_lo, row_hi = 0, 127
        col_lo, col_hi = 0, 7

        for c in line.strip():

            if c == 'B':
                row_lo = 1 + (row_lo + row_hi) // 2
            elif c == 'F':
                row_hi = (row_lo + row_hi) // 2
            elif c == 'R':
                col_lo = 1 + (col_lo + col_hi) // 2
            elif c == 'L':
                col_hi = (col_lo + col_hi) // 2

        assert row_lo == row_hi
        assert col_lo == col_hi

        seat_ids.append(row_lo * 8 + col_lo)

seat_ids = set(seat_ids)

for i in range(min(seat_ids), max(seat_ids) + 1):
    if i not in seat_ids and i-1 in seat_ids and i+1 in seat_ids:
        print(i)
