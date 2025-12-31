def find_missing_letter(chars):
    codes = [ord(c) for c in chars]

    for i in range(len(codes) - 1):
        if codes[i + 1] - codes[i] != 1:
            return chr(codes[i] + 1)
    return None
