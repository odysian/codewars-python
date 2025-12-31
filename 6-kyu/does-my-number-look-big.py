def narcissistic(value):
    digits = str(value)
    power = len(digits)

    return sum(int(d) ** power for d in digits) == value
