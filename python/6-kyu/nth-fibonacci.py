# https://www.codewars.com/kata/522551eee9abb932420004a0/train/python


def nth_fib(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
