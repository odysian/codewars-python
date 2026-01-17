def duplicate_count(text):
    if not text:
        return 0

    freq = {}
    for t in text.lower():
        freq[t] = freq.get(t, 0) + 1

    return sum(1 for v in freq.values() if v > 1)
