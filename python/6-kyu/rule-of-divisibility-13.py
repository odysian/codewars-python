def transform(n):
    seq = [1, 10, 9, 12, 3, 4]
    digits = [int(i) for i in str(n)[::-1]]

    total = 0
    for i, digit in enumerate(digits):
        seq_value = seq[i % len(seq)]
        total += digit * seq_value

    return total


def thirt(n):

    while True:
        new_n = transform(n)

        if new_n == n:
            return n
        n = new_n
