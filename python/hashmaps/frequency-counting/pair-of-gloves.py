# https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python

from collections import Counter


# Build manual hashmap
def number_of_pairs(gloves):
    freq = {}
    for glove in gloves:
        freq[glove] = freq.get(glove, 0) + 1

    pairs = 0
    for f in freq.values():
        pairs += f // 2
    return pairs


# Use Counter to make a hashmap
def number_of_pairs1(gloves):
    count = Counter(gloves)

    return sum(c // 2 for c in count.values())
