def get_count(sentence):

    # Use set for fast lookup
    vowels = {"a", "e", "i", "o", "u"}

    # If char is a vowel, sum it
    return sum(1 for char in sentence if char in vowels)
