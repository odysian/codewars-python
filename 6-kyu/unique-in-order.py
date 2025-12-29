def unique_in_order(sequence):
    res = []

    for s in sequence:
        if not res:
            res.append(s)
        elif s != res[-1]:
            res.append(s)

    return res
