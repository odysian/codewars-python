def longest_repetition(chars):
    if not chars:
        return ("", 0)

    current_char = chars[0]
    current_count = 1

    best_char = chars[0]
    best_count = 1

    for i in range(1, len(chars)):
        char = chars[i]

        if char == current_char:
            current_count += 1
        else:
            if current_count > best_count:
                best_char = current_char
                best_count = current_count

            current_char = char
            current_count = 1

        if current_count > best_count:
            best_char = current_char
            best_count = current_count

    return (best_char, best_count)
