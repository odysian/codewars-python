def validate(n):
    if len(str(n)) > 16:
        return False

    nums = [int(i) for i in str(n)]
    nums.reverse()

    res = []
    for i, num in enumerate(nums):
        # If odd index, double
        if i % 2 == 1:
            dbl = num * 2
            if dbl > 9:
                res.append(dbl - 9)
            else:
                res.append(dbl)
        # If even, append
        else:
            res.append(num)
    return sum(res) % 10 == 0
