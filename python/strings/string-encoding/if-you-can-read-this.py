# https://www.codewars.com/kata/586538146b56991861000293/train/python

from preloaded import NATO  # NATO['A'] == 'Alfa', etc # type: ignore


def to_nato(words: str) -> str:
    out = []
    for char in words.upper():
        if char in NATO:
            out.append(NATO[char])
        elif char != " ":
            out.append(char)
    return " ".join(out)
