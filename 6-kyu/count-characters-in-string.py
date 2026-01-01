def count(s):

    freq = {}

    for l in s:
        freq[l] = freq.get(l, 0) + 1

    return freq
