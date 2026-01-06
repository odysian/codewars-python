def data_reverse(data):
    res = []
    # Loop through 8 bit chunks
    for i in range(0, len(data), 8):
        res.append(data[i : i + 8])
    res.reverse()
    # Flatten list with nested list comprehension
    return [item for sublist in res for item in sublist]
