# https://www.codewars.com/kata/559536379512a64472000053/train/python


def play_pass(s, n):
    res = []
    # Enumerate for index
    for i, char in enumerate(s):
        # If letter, get base ascii, shift, keep within 0-25
        if char.isalpha():
            shift = (ord(char) - ord("A") + n) % 26
            # Back to char
            transformed = chr(shift + ord("A"))
            # Handle upper/lower based on index
            if i % 2 == 0:
                res.append(transformed.upper())
            else:
                res.append(transformed.lower())
        # If number, subtract it from 9 and cast str
        elif char.isdigit():
            res.append(str(9 - int(char)))
        else:
            res.append(char)
    # Join list together in reverse
    return "".join(res[::-1])


# Refactored with helper function to handle transform logic
def play_pass1(s, n):
    def transform(index, char):
        if char.isalpha():
            shifted_code = (ord(char) - ord("A") + n) % 26
            new_char = chr(shifted_code + ord("A"))

            return new_char.upper() if index % 2 == 0 else new_char.lower()

        if char.isdigit():
            return str(9 - int(char))

        return char

    return "".join(transform(i, c) for i, c in enumerate(s))[::-1]
