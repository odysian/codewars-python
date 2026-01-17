def up_array(arr):
    if not arr:
        return None

    for digit in arr:
        if digit < 0 or digit > 9:
            return None

    num_str = "".join(str(d) for d in arr)
    num = int(num_str)
    num += 1

    result_str = str(num).zfill(len(arr))

    return [int(d) for d in result_str]
