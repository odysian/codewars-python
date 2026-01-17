# https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python


def reverse_alternate(st):
    words = st.split()
    res = []
    for i, w in enumerate(words):
        if i % 2 == 1:
            res.append(w[::-1])
        else:
            res.append(w)
    return " ".join(res)

    # One liner
    return " ".join([w[::-1] if i % 2 else w for i, w in enumerate(st.split())])
