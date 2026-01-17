def is_valid_IP(strng):
    octets = strng.split(".")

    if len(octets) != 4:
        return False

    for o in octets:
        if not o.isdigit():
            return False
        if o.startswith("0") and len(o) > 1:
            return False
        if not (0 <= int(o) <= 255):
            return False

    return True
