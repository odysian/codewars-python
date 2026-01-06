def duplicate_encode(word):
    seen = set()
    dupes = set()

    for w in word.lower():
        if w in seen:
            dupes.add(w)
        seen.add(w)

    return "".join(")" if w in dupes else "(" for w in word.lower())
