def rot13(message):
    res = []
    for m in message:
        # If letter
        if m.isalpha():
            # Get base ascii value for lower and upper
            base = ord("a") if m.islower() else ord("A")
            # Get value of letter in 0-25 alphabet
            alpha_idx = ord(m) - base
            # Rotate by 13, modulo by 26 if goes over
            new_index = (alpha_idx + 13) % 26
            # Convert back to chr
            res.append(chr(new_index + base))
        else:
            res.append(m)
    return "".join(res)
