def rev_rot(strng, sz):
    # Validation
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""

    res = []
    # Calculate limit: how many full chunks can we fit?
    limit = (len(strng) // sz) * sz
    for s in range(0, limit, sz):
        chunk = strng[s : s + sz]
        # If sum of digits divisible by 2, reverse
        if sum(int(c) for c in chunk) % 2 == 0:
            res.append(chunk[::-1])
        # Else rotate one position left
        else:
            res.append(chunk[1:] + chunk[0])
    return "".join(res)
