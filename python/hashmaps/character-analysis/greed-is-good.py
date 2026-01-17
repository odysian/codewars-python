# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

from collections import Counter, defaultdict


def score(dice):
    # Use counter for freq map
    freq = Counter(dice)
    score = 0
    # Score dict for triplet lookup
    triplet_scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

    # Process freq, handle triplet scoring and removal
    for die_value, count in freq.items():
        if count >= 3:
            score += triplet_scores[die_value]
            freq[die_value] -= 3

    # Handle leftover 1s and 5s
    score += freq[1] * 100 + freq[5] * 50
    return score


def score1(dice):
    # Default dict so we dont have to use .get()
    freq = defaultdict(int)
    score = 0

    for d in dice:
        freq[d] += 1
        # Handle triplets on the fly
        if freq[d] >= 3:
            if d == 1:
                score += 1000
            else:
                score += d * 100
            freq[d] -= 3
    # Handle leftover 1s and 5s
    score += freq[1] * 100 + freq[5] * 50
    return score
