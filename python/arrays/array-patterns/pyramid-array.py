# https://www.codewars.com/kata/515f51d438015969f7000013/train/python


def pyramid(n):
    res = []
    for i in range(1, n + 1):
        res.append([1] * i)
    return res


def pyramid1(n):
    return [[1] * i for i in range(1, n + 1)]
