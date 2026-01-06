def find_nb(m):
    # Start with 1
    n = 1
    total = 0
    # Loop until we equal or go past m
    while total < m:
        # Cube n and add to total
        total += n**3
        if total == m:
            return n
        n += 1
    return -1
