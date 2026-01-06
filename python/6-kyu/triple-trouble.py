# https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/python


def triple_double(num1, num2):
    n1 = str(num1)
    n2 = str(num2)

    # Loop through each number
    for i in range(10):
        s = str(i)
        # Use string membership check
        if (s * 3) in n1 and (s * 2) in n2:
            return 1
    return 0
