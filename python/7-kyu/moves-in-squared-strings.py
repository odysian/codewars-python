def vert_mirror(strng):

    # Split into lines, reverse the line, then join
    return "\n".join(line[::-1] for line in strng.split("\n"))


def hor_mirror(strng):

    # Split string on \n, reverse list, then join
    return "\n".join(strng.split("\n")[::-1])


def oper(fct, s):

    return fct(s)
