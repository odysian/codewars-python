def expanded_form(num):
    res = []
    # Work with string number
    str_num = str(num)

    # Enum to get index and digit
    for i, digit in enumerate(str_num):
        if digit != "0":
            # Calc place value
            place_value = int(digit) * 10 ** (len(str_num) - i - 1)
            res.append(str(place_value))

    return " + ".join(res)
