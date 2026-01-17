def stray(arr):
    hashmap = {}

    # Count num in arr, add to hashmap
    for i in arr:
        hashmap[i] = hashmap.get(i, 0) + 1

    # Find value with count of 1
    for i in arr:
        if hashmap[i] == 1:
            return i
    return None
