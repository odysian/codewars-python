def dig_pow(n, p):
    digits = [int(i) for i in str(n)]

    total = 0
    for i, digit in enumerate(digits):
        total += digit ** (p + i)

    return total // n if total % n == 0 else -1
