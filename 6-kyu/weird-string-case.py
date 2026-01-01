# Initial
def to_weird_case(words):
    word_list = words.split()
    res = []
    # Loop each word
    for word in word_list:
        char_list = []
        # Enum each char
        for i, char in enumerate(word):
            # If even, upper. Else, lower
            if i % 2 == 0:
                char = char.upper()
            else:
                char = char.lower()
            # Build list with chars
            char_list.append(char)

        # Build word with char_list
        res.append("".join(char_list))
    return " ".join(res)


# Refactor with comprehension
def to_weird_case2(words):

    def weirdify(word):
        return "".join(
            char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(word)
        )

    return " ".join(weirdify(w) for w in words.split())
