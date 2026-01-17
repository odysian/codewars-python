def encrypt_this(text):
    if not text:
        return ""
    res = []

    for word in text.split():
        first = str(ord(word[0]))

        if len(word) == 1:
            enc_word = first
        elif len(word) == 2:
            enc_word = first + word[1]
        else:
            enc_word = first + word[-1] + word[2:-1] + word[1]
        res.append(enc_word)
    return " ".join(res)
