def highest_rank(arr):
    freq = {}
    for a in arr:
        freq[a] = freq.get(a, 0) + 1
    # Lambda key checks the count then the dict key
    return max(freq, key=lambda k: (freq[k], k))
