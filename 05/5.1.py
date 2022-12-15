max_seat_id = -1

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

            print(f'{c} {row_lo} {row_hi} {col_lo} {col_hi}')

        assert row_lo == row_hi
        assert col_lo == col_hi

        seat_id = row_lo * 8 + col_lo

        max_seat_id = max(max_seat_id, seat_id)

        print(seat_id)
        print()

print(max_seat_id)
