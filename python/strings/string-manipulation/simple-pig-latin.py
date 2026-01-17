def pig_it(text):
    words = text.split()
    res = []
    for word in words:
        if word.isalpha():
            word = word[1:] + word[0] + "ay"
            res.append(word)
        else:
            res.append(word)

    return " ".join(res)
