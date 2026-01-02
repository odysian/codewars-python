def good_vs_evil(good, evil):
    good_values = [1, 2, 3, 3, 4, 10]
    evil_values = [1, 2, 2, 2, 3, 5, 10]

    good_sum = sum(v * int(c) for v, c in zip(good_values, good.split()))
    evil_sum = sum(v * int(c) for v, c in zip(evil_values, evil.split()))

    if good_sum > evil_sum:
        return "Battle Result: Good triumphs over Evil"
    elif good_sum < evil_sum:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"
