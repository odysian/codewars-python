def persistence(n):
    if n < 10:
        return 0

    mults = 0
    res = n

    while res >= 10:
        product = 1
        for digit in str(res):
            product *= int(digit)
        res = product
        mults += 1
    return mults
