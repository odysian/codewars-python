def parts_sums(ls):
    if not ls:
        return [0]

    total = sum(ls)
    res = [total]

    for value in ls:
        total -= value
        res.append(total)

    return res
