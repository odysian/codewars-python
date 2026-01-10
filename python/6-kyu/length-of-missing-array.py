# https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611/train/python


def get_length_of_missing_array(arrays):
    # Validation
    if not arrays or len(arrays) < 2:
        return 0
    for arr in arrays:
        if arr is None or len(arr) == 0:
            return 0

    # Sort arrays by len
    arrays.sort(key=len)
    for i in range(len(arrays) - 1):
        # Compare array to the next one, if the len isnt +1, we return
        if len(arrays[i]) + 1 != len(arrays[i + 1]):
            return len(arrays[i]) + 1
