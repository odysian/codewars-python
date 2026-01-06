def clean_string(s):
    res = []

    for i in s:
        if i != "#":
            res.append(i)
        elif res:
            res.pop()
    return "".join(res)
