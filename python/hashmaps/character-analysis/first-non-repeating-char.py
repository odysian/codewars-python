def first_non_repeating_letter(strng):
    freq = {}
    # Count both upper/lower chars together
    for s in strng:
        st = s.lower()
        freq[st] = freq.get(st, 0) + 1

    # Check for first count that equals 1
    for s in strng:
        if freq[s.lower()] == 1:
            # Return the original case of the char
            return s

    return ""
