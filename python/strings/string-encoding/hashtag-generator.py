def generate_hashtag(s):
    words = s.split()
    # Validation handles both empty strings and whitespace
    if not words:
        return False
    # Capitalize and join each word
    hashtag = "#" + "".join(w.capitalize() for w in words)
    # Check length after creating hashtag
    return hashtag if len(hashtag) <= 140 else False
