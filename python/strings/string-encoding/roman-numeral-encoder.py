def solution(n):
    # List of ordered tuples to iterate through
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    res = ""
    # Unpack tuples
    for value, numeral in values:
        # See how many times value can be subtracted
        count = n // value

        if count:
            # If value fits, add numeral x times to result
            res += numeral * count
            # Subtract value x times from num
            n -= value * count
    return res
