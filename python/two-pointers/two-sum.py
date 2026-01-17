def two_sum(numbers, target):
    seen = {}

    for i, num in enumerate(numbers):
        seeking = target - num
        if seeking in seen:
            return (seen[seeking], i)
        seen[num] = i
