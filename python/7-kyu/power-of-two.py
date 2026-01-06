def power_of_two(x):
    if x <= 0:
        return False

    while x % 2 == 0:
        x = x // 2
    return x == 1


#     Bitwise trick
#     return x > 0 and (x & (x - 1) == 0)
