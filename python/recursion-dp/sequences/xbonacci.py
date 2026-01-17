# https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python


def xbonacci(sig, n):
    #     # append sum() of sig[i: sig.length + i] until sig.length = n

    res = sig[:]
    for i in range(n - len(sig)):
        res.append(sum(res[i : len(sig) + i]))
    return res[:n]


def xbonacci1(sig, n):
    # subtract first number, add new value to sum each iteration
    res = sig[:]
    length = len(sig)
    # Take initial sum
    curr_sum = sum(res)
    for i in range(n - length):
        # The next value we add is the current sum
        next_val = curr_sum
        res.append(next_val)
        # Subtract digit from earliest place each iteration
        # Add the newest digit to get a new running total for window
        curr_sum = curr_sum - res[i] + next_val
    return res[:n]
