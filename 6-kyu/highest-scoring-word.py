def high(x):
    # Split words into list
    words = x.split()

    # Init high score vars
    high_score = 0
    high_score_word = ""

    for word in words:
        # Sum the score of each char in a word
        total_score = sum(ord(char) - ord("a") + 1 for char in word)

        # Check if high score
        if total_score > high_score:
            high_score = total_score
            high_score_word = word

    return high_score_word
