from collections import Counter


def find_uniq(arr):

    # Set tracking
    seen = set()
    dupes = set()

    for num in arr:
        if num in seen:
            dupes.add(num)
        else:
            seen.add(num)

    for num in seen:
        if num not in dupes:
            return num
    return []

    # Counter

    counts = Counter(arr)
    for num, count in counts.items():
        if count == 1:
            return num
