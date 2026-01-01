# Initial attempt with di_count
def diamond(n):
    if n % 2 == 0 or n < 0:
        return None

    di_count = 1
    res = ""

    for i in range(n):
        # Calc spaces by using n as total width
        spaces = " " * ((n - di_count) // 2)
        stars = "*" * di_count

        # If center of diamond
        if di_count == n:
            res += ("*" * di_count) + "\n"
            di_count -= 2
        # Else if top of diamond (Adding diamonds after)
        elif i < n // 2:
            res += f"{spaces}{stars}\n"
            di_count += 2
        # Else bottom of diamond (Removing diamonds after)
        else:
            res += f"{spaces}{stars}\n"
            di_count -= 2

    return res


# Mathy approach
def diamond2(n):

    # Get center of diamond
    center = n // 2
    lines = []

    for i in range(n):
        # Distance from center of diamond
        dist = abs(center - i)
        # Distance always equals empty spaces
        spaces = " " * dist
        # Stars equals width - 2 * distance
        stars = "*" * (n - (2 * dist))
        lines.append(spaces + stars + "\n")

    return "".join(lines)
