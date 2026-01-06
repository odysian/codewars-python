# Set lookup
def in_array(array1, array2):

    seen = set()
    res = []
    for a1 in array1:
        if a1 in seen:
            continue
        for a2 in array2:
            if a1 in a2:
                res.append(a1)
                seen.add(a1)
                break

    return sorted(res)


# Set comprehension with any
def in_array2(array1, array2):
    return sorted({a1 for a1 in array1 if any(a1 in a2 for a2 in array2)})
