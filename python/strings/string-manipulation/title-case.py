def title_case(title, minor_words=""):
    if not title:
        return ""

    # Use set for membership check
    minor = set(minor_words.lower().split())
    words = title.lower().split()

    return " ".join(
        word.capitalize() if i == 0 or word not in minor else word
        for i, word in enumerate(words)
    )
