def find_even_index(arr):

    # BRUTE FORCE
    # Recalculates sum every loop
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1 :])
        if left_sum == right_sum:
            return i
    return -1

    # SMART
    # Sums total, checks if right equals total - left
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]

    return -1
