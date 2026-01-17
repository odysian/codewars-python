def fold_array(array, runs):

    def fold_once(array):

        if len(array) == 1:
            return array

        # Find middle, split left side
        mid = len(array) // 2
        left = array[:mid]

        # If odd length, set middle and split right
        if len(array) % 2 == 1:
            middle = array[mid]
            right = array[mid + 1 :]
        # If even, set right to include middle
        else:
            middle = None
            right = array[mid:]

        # Reverse right side for folding
        right_reversed = right[::-1]

        res = []
        for i in range(len(left)):
            res.append(left[i] + right_reversed[i])

        # If odd len, add the unfolded middle to the end
        if middle is not None:
            res.append(middle)

        return res

    # Copy array
    result = array[:]

    for _ in range(runs):
        result = fold_once(result)

    return result
