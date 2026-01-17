MORSE_CODE = {}


def decode_morse(morse_code):
    morse_code = morse_code.strip()
    words = morse_code.split("   ")

    decoded_words = []
    for word in words:
        letters = word.split()

        decoded_letters = []
        for letter in letters:
            if letter in MORSE_CODE:
                decoded_letters.append(MORSE_CODE[letter])

        decoded_word = "".join(decoded_letters)
        decoded_words.append(decoded_word)

    return " ".join(decoded_words)
