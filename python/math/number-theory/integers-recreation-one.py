# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python


def list_squared(m, n):
    res = []
    # Loop through m -> n
    for num in range(m, n + 1):
        # Nested loop to store divisors of current num
        divisors = []
        # Since divisors come in pairs, only check up to the square root
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                # Check for perfect squares so not adding duplicates
                if i != num // i:
                    divisors.append(num // i)
        # Sum the divisors, take sqrt of sum and cast int
        # If perfect square, int wont change the value
        sum_of_squares = sum(d**2 for d in divisors)
        sqrt = int(sum_of_squares**0.5)
        # If int changed it, equality check will return False
        if sqrt * sqrt == sum_of_squares:
            res.append([num, sum_of_squares])
    return res
