# https://www.codewars.com/kata/54a2e93b22d236498400134b/train/python


# Map keys to a list of strings
def presses(phrase):
    keys = [
        "1",
        "ABC2",
        "DEF3",
        "GHI4",
        "JKL5",
        "MNO6",
        "PQRS7",
        "TUV8",
        "WXYZ9",
        "*",
        " 0",
        "#",
    ]

    total = 0
    phrase = phrase.upper()

    for char in phrase:
        for key in keys:
            if char in key:
                # Use index in string as number of presses
                total += key.index(char) + 1
                break
    return total
