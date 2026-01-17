# https://www.codewars.com/kata/5274e122fc75c0943d000148/train/python


def group_by_commas(n):
    # num to string, reverse it
    s = str(n)[::-1]

    if len(s) < 4:
        return str(n)
    # Build chunks by steps of 3
    chunks = []
    for i in range(0, len(s), 3):
        chunks.append(s[i : i + 3])
    # Join chunks with commas, reverse
    return ",".join(chunks)[::-1]
