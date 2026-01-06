def parse(data):
    num = 0
    res = []
    for i in data:
        if i == "i":
            num += 1
        elif i == "d":
            num -= 1
        elif i == "s":
            num *= num
        elif i == "o":
            res.append(num)
    return res


# Match case
def parse2(data):
    num = 0
    res = []

    for command in data:
        match command:
            case "i":
                num += 1
            case "d":
                num -= 1
            case "s":
                num *= num
            case "o":
                res.append(num)
            case _:
                pass
    return res
