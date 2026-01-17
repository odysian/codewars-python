def sort_array(source_array):

    odd_nums = sorted([s for s in source_array if s % 2 == 1])
    odd_counter = 0

    res = source_array[:]
    for i, s in enumerate(res):
        if s % 2 == 1:
            res[i] = odd_nums[odd_counter]
            odd_counter += 1

    return res
