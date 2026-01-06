def factorial(n):
    if 12 < n or n < 0:
        raise ValueError
    if n == 0:
        return 1

    # Start from 1, multiply our way up to n
    # Mult and add to res each loop
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res
