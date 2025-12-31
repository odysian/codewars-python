def to_camel_case(text):
    if not text:
        return ""

    words = text.replace("-", " ").replace("_", " ").split()

    first = words[0]
    rest = [word.title() for word in words[1:]]

    return first + "".join(rest)
