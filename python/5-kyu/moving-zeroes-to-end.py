# Build two lists, concat them
def move_zeros(lst):
    nums = []
    zeroes = []
    for l in lst:
        if l != 0:
            nums.append(l)
        else:
            zeroes.append(l)
    return nums + zeroes


# Use .sort()
def move_zeoes2(lst):
    lst.sort(key=lambda x: x == 0)
    return lst
