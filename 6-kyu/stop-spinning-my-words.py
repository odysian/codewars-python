def spin_words(sentence):
    word_list = sentence.split()

    res = []
    for word in word_list:
        if len(word) >= 5:
            res.append(word[::-1])
        else:
            res.append(word)
    return " ".join(res)
