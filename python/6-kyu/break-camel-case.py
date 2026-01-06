def solution(s):
    res = []
    for char in s:
        if char.isupper():
            res.append(" ")
        res.append(char)

    return "".join(res).strip()
