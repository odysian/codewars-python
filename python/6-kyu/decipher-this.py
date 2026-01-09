# https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python
import re


# First attempt (Messy)
def decipher_this(s):
    res = []
    for word in s.split():
        new_word = ""
        code = ""
        if word.isdigit():
            res.append(chr(int(word)))
            continue
        for i, char in enumerate(word):
            if not char.isdigit():
                first = chr(int(word[:i]))
                second = word[i]
                letters = word[i:]
                last = word[-1]

                if len(letters) == 0:
                    new_word = first
                elif len(letters) == 1:
                    new_word = first + second
                elif len(letters) == 2:
                    new_word = first + last + second
                else:
                    new_word = first + last + letters[1:-1] + second
                break

        res.append(new_word)

    return " ".join(res)


# Refactor
def decipher_this1(s):
    res = []
    for word in s.split():
        i = 0
        while i < len(word) and word[i].isdigit():
            i += 1
        code = word[:i]
        letters = list(word[i:])

        first_char = chr(int(code))

        if len(letters) >= 2:
            letters[0], letters[-1] = letters[-1], letters[0]

        res.append(first_char + "".join(letters))

    return " ".join(res)


# Regex


def decipher_this2(s):
    res = []

    for word in s.split():
        # ^(\d+) -> Start with digits (Group 1)
        # (.*)$  -> Everything else (Group 2)
        match = re.match(r"^(\d+)(.*)$", word)
        char_code, letters = match.groups()  # type: ignore

        # 2. Decode the first letter
        first_letter = chr(int(char_code))

        # 3. Swap logic (Only needed if we have letters)
        if len(letters) >= 2:
            # Reconstruct: First + Last + Middle + Second
            letters = letters[-1] + letters[1:-1] + letters[0]

        res.append(first_letter + letters)

    return " ".join(res)
