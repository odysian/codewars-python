from collections import Counter


# Counter Approach
def scramble(s1, s2):
    supply = Counter(s1)
    recipe = Counter(s2)

    for char, count in recipe.items():
        if supply[char] < count:
            return False
    return True


# Dict Freq Map
def scramble1(s1, s2):
    supply = {}
    recipe = {}

    for s in s1:
        supply[s] = supply.get(s, 0) + 1

    for s in s2:
        recipe[s] = recipe.get(s, 0) + 1

    for r in recipe:
        if supply.get(r, 0) < recipe[r]:
            return False
    return True
