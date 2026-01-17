# https://www.codewars.com/kata/57f625992f4d53c24200070e/train/python

# Checking if the chr(number) is in the string is faster than looping
# and checking if the letters equal the number


def bingo(ticket, win):
    mini_wins = 0
    for string, number in ticket:
        if chr(number) in string:
            mini_wins += 1
    if mini_wins >= win:
        return "Winner!"
    return "Loser!"
