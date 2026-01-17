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


# CODING MEETUP 8
def all_continents(lst):

    REQUIRED = {"Africa", "Americas", "Asia", "Europe", "Oceania"}

    found = {dev["continent"] for dev in lst}

    return found >= REQUIRED


# CODING MEETUP 9
def is_age_diverse(lst):
    required_decades = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    found_decades = {min(dev["age"] // 10, 10) for dev in lst}

    return found_decades >= required_decades


from datetime import datetime


# CODING MEETUP 10
def add_username(lst):

    current_year = datetime.now().year

    for dev in lst:

        birth_year = current_year - dev["age"]

        p1 = dev["firstName"].lower()

        p2 = dev["lastName"][0].lower()

        dev["username"] = f"{p1}{p2}{birth_year}"

    return lst
