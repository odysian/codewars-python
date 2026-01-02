data = "Hi! My name is Chris"


def buffer(sentence):
    buffer = ""
    res = []

    for s in sentence:
        if s.isalnum():
            buffer += s
        else:
            if buffer:
                res.append(buffer[::-1])
                buffer = ""

            res.append(s)
    if buffer:
        res.append(buffer[::-1])

    print(res)
    print("".join(res))

    return res


def main():
    buffer(data)
    return None


main()
