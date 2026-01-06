def find_it(seq):
    if not seq:
        return None

    count = {}

    for i in seq:
        count[i] = count.get(i, 0) + 1

    for num, c in count.items():
        if c % 2 == 1:
            return num
