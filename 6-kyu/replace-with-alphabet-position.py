def alphabet_position(text):
    base = ord("a") - 1
    pos = [ord(t) - base for t in text.lower() if t.isalpha()]
    return " ".join(str(p) for p in pos)
