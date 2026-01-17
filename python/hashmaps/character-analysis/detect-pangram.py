def is_pangram(st):
    result = {s for s in st.lower() if s.isalpha()}

    return len(result) == 26
