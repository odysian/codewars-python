def multiplication_table(size):
    res = []

    for i in range(1, size + 1):
        line = []
        for j in range(1, size + 1):
            line.append(i * j)
        res.append(line)
    return res


def multiplcation_table2(size):
    return [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]
