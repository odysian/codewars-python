def tower_builder(n_floors):

    # MANUAL BUILD
    total_width = (n_floors * 2) - 1
    stars = 1

    res = []
    for i in range(n_floors):
        empty = (total_width - stars) // 2

        res.append((" " * empty) + ("*" * stars) + (" " * empty))
        stars += 2

    return res

    # USE .center() to create padding
    width = n_floors * 2 - 1
    res = []
    for n in range(n_floors):
        res.append(("*" * (2 * n + 1)).center(width))

    return res
