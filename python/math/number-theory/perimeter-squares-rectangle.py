# https://www.codewars.com/kata/559a28007caad2ac4e000083/train/python


def perimeter(n):
    # Use Fibonacci seq, preload first number into total
    a = 0
    b = 1
    total = 1
    for i in range(n):
        total += a + b
        a, b = b, a + b
    return total * 4
