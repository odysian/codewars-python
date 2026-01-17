# https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python


def kebabize(st):
    out = []
    for s in st:
        if s.isupper():
            out.append(f"-{s.lower()}")
        elif s.isdigit():
            continue
        else:
            out.append(s)
    return "".join(out).lstrip("-")


# Comprehension
def kebabize1(st):
    result = "".join(
        f"-{s.lower()}" if s.isupper() else s for s in st if not s.isdigit()
    )
    return result.lstrip("-")
