def decrypt_once(s):
    if not s:
        return s

    mid = len(s) // 2
    odds = s[:mid]
    evens = s[mid:]

    result = ""

    for i in range(len(odds)):
        result += evens[i]
        result += odds[i]
    if len(evens) > len(odds):
        result += evens[-1]
    return result


def decrypt(encrypted_text, n):

    result = encrypted_text
    for _ in range(n):
        result = decrypt_once(result)

    return result


def encrypt_once(text):
    odds = ""
    evens = ""

    for i, char in enumerate(text):
        if i % 2 == 0:
            evens += char
        else:
            odds += char

    return odds + evens


def encrypt(text, n):
    if not text or n <= 0:
        return text

    result = text
    for _ in range(n):
        result = encrypt_once(result)

    return result
