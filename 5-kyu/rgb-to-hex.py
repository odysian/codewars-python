# Initial Attempt
def rgb1(r, g, b):
    hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    rgb = [r, g, b]

    res = []
    for i in rgb:
        if i < 0:
            i = 0
        if i > 255:
            i = 255
        hex1, hex2 = divmod(i, 16)
        if hex1 > 9:
            hex1 = hex_map[hex1]
        if hex2 > 9:
            hex2 = hex_map[hex2]
        res.append([hex1, hex2])
    return "".join([str(item) for sublist in res for item in sublist])


# Refactor
def rgb2(r, g, b):
    hex_map = "0123456789ABCDEF"
    rgb = [r, g, b]

    res = []
    for i in rgb:
        # Better way to clamp value than initial
        i = max(0, min(i, 255))

        hex1, hex2 = divmod(i, 16)
        # Lookup in hex map vs dict
        res.append(hex_map[hex1])
        res.append(hex_map[hex2])
    return "".join(res)


# Pythonic way
def rgb3(r, g, b):
    def clamp(x):
        return max(0, min(x, 255))

    return "{:02X}{:02X}{:02X}".format(clamp(r), clamp(g), clamp(b))
