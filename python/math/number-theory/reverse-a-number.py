def reverse_number(n):
    # Get absolute value, convert to str and reverse
    reversed_string = str(abs(n))[::-1]

    # If n is negative, mult by -1 and return
    return int(reversed_string) * (-1 if n < 0 else 1)
