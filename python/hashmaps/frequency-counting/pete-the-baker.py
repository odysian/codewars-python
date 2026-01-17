# First solution
def cakes(recipe, available):

    count = []
    for r in recipe:
        if r in available:
            count.append(available[r] // recipe[r])
        else:
            return 0
    return min(count)


# Dict get() solution
def cakes1(recipe, available):

    count = []
    for i, a in recipe.items():
        count.append(available.get(i, 0) // a)
    return min(count)


# One liner
def cakes2(recipe, available):

    return min(available.get(i, 0) // a for i, a in recipe.items())
