# https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python


def pascals_triangle(n):
    res = []
    row = [1]
    for _ in range(n):
        res.extend(row)

        next_row = [1]
        for i in range(len(row) - 1):
            window_sum = row[i] + row[i + 1]
            next_row.append(window_sum)

        next_row.append(1)
        row = next_row

    return res
