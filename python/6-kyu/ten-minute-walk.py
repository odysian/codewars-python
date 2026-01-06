def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    # x and y coords
    coords = [0, 0]

    for w in walk:
        if w == "n":
            coords[1] += 1
        elif w == "s":
            coords[1] -= 1
        elif w == "e":
            coords[0] += 1
        elif w == "w":
            coords[0] -= 1

    return coords == [0, 0]
