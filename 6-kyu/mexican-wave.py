def wave(people):
    if not people:
        return []

    res = []
    for i, p in enumerate(people):
        if p == " ":
            continue

        res.append(people[:i] + p.upper() + people[i + 1 :])

    return res
