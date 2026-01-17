from collections import defaultdict


def delete_nth(order, max_e):

    # Defaultdict to init missing keys to 0
    freq = defaultdict(int)
    res = []

    for num in order:
        # Add 1 each time we see a num
        freq[num] += 1

        # If count less than or equal, we append
        if freq[num] <= max_e:
            res.append(num)

    return res
