def get_sum(a, b):
    # Use min/max to order a/b for proper range, them sum
    return sum(range(min(a, b), max(a, b) + 1))
