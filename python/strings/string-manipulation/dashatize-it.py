# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python


def dashatize(n):
    if n is None:
        return "None"
    # Convert abs to str to clean potential negative
    str_n = str(abs(n))

    d_list = []
    for digit in str_n:
        # If odd, add dashes. Else just the digit. Append
        if int(digit) % 2 == 1:
            d_list.append("-" + digit + "-")
        else:
            d_list.append(digit)
    # Join together, strip leading and trailing dashes, replace dbls with single
    return "".join(d_list).lstrip("-").rstrip("-").replace("--", "-")
