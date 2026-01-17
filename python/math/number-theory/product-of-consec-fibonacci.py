# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python


def product_fib(prod):
    a, b = 0, 1

    # Until we reach or exceed prod
    while a * b < prod:
        # Fibonacci sequence
        # a becomes b
        # b becomes sum of previous two
        a, b = b, a + b

    return [a, b, a * b == prod]
