def sum_dig_pow(a, b):
    res = []
    # Loop through number range, include b
    for num in range(a, b + 1):
        # Conver numbers to list of digits
        digits = [int(s) for s in str(num)]
        # Add up the digits raised to consec powers
        total = sum(d ** (idx + 1) for idx, d in enumerate(digits))
        # Append to results
        if total == num:
            res.append(num)

    return res
