# https://www.codewars.com/kata/5375f921003bf62192000746/train/python


def abbreviate(strng):
    # Helper function to cut down repetition
    def shorten(word):
        if len(curr_word) >= 4:
            return word[0] + str(len(curr_word) - 2) + word[-1]
        return word

    res = []
    curr_word = ""

    for char in strng:
        # If letter build word
        if char.isalpha():
            curr_word += char
        else:
            # If not letter, call helper, append non letter, clear curr
            if curr_word:
                res.append(shorten(curr_word))
            res.append(char)
            curr_word = ""
    # Handle final word if string ends on a letter
    if curr_word:
        res.append(shorten(curr_word))
    return "".join(res)
