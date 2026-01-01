def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ""

    word_list = []
    for i in range(len(strarr) - k + 1):

        word = []
        for j in range(k):
            word.append(strarr[i + j])

        word_list.append("".join(word))

    res = sorted(word_list, key=len, reverse=True)
    return res[0]
