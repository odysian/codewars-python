# https://www.codewars.com/kata/59f08f89a5e129c543000069/train/python


def dup(arry):
    res = []
    for word in arry:
        clean_word = []
        last_seen = None
        for char in word:
            if char != last_seen:
                clean_word.append(char)
            last_seen = char
        res.append("".join(clean_word))
    return res
