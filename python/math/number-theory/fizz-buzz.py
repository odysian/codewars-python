def fizzbuzz(n):

    res = []

    for i in range(1, n + 1):
        word = ""

        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"

        res.append(word or i)

    return res
