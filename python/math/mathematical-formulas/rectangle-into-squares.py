def sq_in_rect(l, w):
    # If square, return none
    if l == w:
        return None

    res = []
    # While we have dimensions
    while l > 0 and w > 0:
        # Add smaller side to list then subtract it from larger side
        if l < w:
            res.append(l)
            w -= l
        else:
            res.append(w)
            l -= w
    return res
