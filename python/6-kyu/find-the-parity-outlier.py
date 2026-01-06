def find_outlier(integers):
    first_three = integers[:3]
    odd_count = sum(1 for x in first_three if x % 2 == 1)

    if odd_count >= 2:
        return next(x for x in integers if x % 2 == 0)
    else:
        return next(x for x in integers if x % 2 == 1)
