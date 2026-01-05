# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python

from itertools import combinations


def choose_best_sum(t, k, ls):
    # Use itertools.combinations
    # Without library would have to manage k nested loops
    all_combos = combinations(ls, k)
    valid_sums = []
    # Sum the combo, if its within the limit: append
    for combo in all_combos:
        total = sum(combo)
        if sum(combo) <= t:
            valid_sums.append(total)
    return max(valid_sums) if valid_sums else None
