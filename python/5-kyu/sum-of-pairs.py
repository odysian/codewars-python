# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python


def sum_pairs(ints, s):
    # Use set since we don't need indexes
    seen = set()
    for i in ints:
        if s - i in seen:
            return [s - i, i]
        seen.add(i)
    return None
