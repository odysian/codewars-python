# CODING MEETUP 1
def count_developers(lst):
    # Sum 1 for every developer where continent is Europe AND language is JS
    return sum(
        1
        for dev in lst
        if dev["continent"] == "Europe" and dev["language"] == "JavaScript"
    )


# CODING MEETUP 2
def greet_developers(lst):

    for dev in lst:
        dev["greeting"] = (
            f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"
        )

    return lst


# CODING MEETUP 3
def is_ruby_coming(lst):

    return any(dev["language"] == "Ruby" for dev in lst)


# CODING MEETUP 4
def get_first_python(users):

    #     for dev in users:
    #         if dev['language'] == 'Python':
    #             return f"{dev['first_name']}, {dev['country']}"
    #     return "There will be no Python developers"

    return next(
        (
            f"{dev['first_name']}, {dev['country']}"
            for dev in users
            if dev["language"] == "Python"
        ),
        "There will be no Python developers",
    )


# CODING MEETUP 5
def count_languages(lst):
    counts = {}

    for dev in lst:
        lang = dev["language"]

        counts[lang] = counts.get(lang, 0) + 1

    return counts


# CODING MEETUP 6
def is_same_language(lst):

    # === Set() and check for more than one value: SLOWER ===
    # res = set()

    # for dev in lst:
    #     lang = dev['language']
    #     res.add(lang)

    # if len(res) == 1:
    #     return True
    # return False

    # === Set Comprehension ===

    # return len({dev['language'] for dev in lst}) == 1

    # === all() to check that first value matches all values: FASTER ===
    if not lst:
        return True

    first_lang = lst[0]["language"]

    return all(dev["language"] == first_lang for dev in lst)


# CODING MEETUP 7


def find_senior(lst):
    # === KING OF THE HILL ===
    # res = []
    # current_max_age = 0

    # for dev in lst:
    #     age = dev['age']

    #     # if age is higher than current, wipe list and set new current
    #     if age > current_max_age:
    #         current_max_age = age
    #         res = [dev]

    #     # if age is the same, append
    #     elif age == current_max_age:
    #         res.append(dev)

    # return res

    # === TWO PASS, record max, then match those == max ===

    max_age = max(dev["age"] for dev in lst)

    return [dev for dev in lst if dev["age"] == max_age]
