def bubble_sort(n):
    n_l = len(n)

    for i in range(n_l):
        for j in range(n_l - 1 - i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

    return n


print(bubble_sort([4, 7, 2, 1, 8]))
