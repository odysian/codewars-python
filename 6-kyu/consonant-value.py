def solve(s):
    vowels = {"a", "e", "i", "o", "u"}
    for v in vowels:
        s = s.replace(v, " ")

    groups = s.split()

    high_score = 0
    for g in groups:
        score = sum(ord(l) - 96 for l in g)

        if score > high_score:
            high_score = score

    return high_score
