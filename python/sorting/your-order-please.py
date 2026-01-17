def order(sentence):
    words = sentence.split()
    my_dict = {}

    for word in words:
        for char in word:
            if char.isnumeric():
                my_dict[int(char)] = word
                break

    return " ".join(my_dict[k] for k in sorted(my_dict.keys()))
