def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    if len(array1) != len(array2):
        return False

    array1.sort(key=abs)
    array2.sort(key=abs)

    for i, a in enumerate(array1):
        if a**2 != array2[i]:
            return False

    return True
