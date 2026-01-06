def count_deaf_rats(town):
    p_index = 0
    count = 0
    for i, t in enumerate(town):
        if t == "P":
            p_index = i

    left = town[:p_index]
    left_no_spaces = left.replace(" ", "")
    right = town[p_index + 1 :]
    right_no_spaces = right.replace(" ", "")

    for i in range(0, len(left_no_spaces), 2):
        rat = left_no_spaces[i : i + 2]
        if rat == "O~":
            count += 1

    for i in range(0, len(right_no_spaces), 2):
        rat = right_no_spaces[i : i + 2]
        if rat == "~O":
            count += 1

    return count
