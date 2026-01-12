# https://www.codewars.com/kata/5d23d89906f92a00267bb83d/train/python


def get_order(order):
    # create hashmap of menu
    # create pointers, one scans ahead until it finds a slice that matches an item in the set
    # reset pointer to 1+ right pointers index
    # Use lambda to sort by menu values

    menu = {
        "Burger": 0,
        "Fries": 1,
        "Chicken": 2,
        "Pizza": 3,
        "Sandwich": 4,
        "Onionrings": 5,
        "Milkshake": 6,
        "Coke": 7,
    }
    res = []
    l = 0
    r = 1
    while r <= len(order):
        if order[l:r].title() in menu:
            res.append(order[l:r].title())
            l = r
            r = l + 1
        else:
            r += 1
    res.sort(key=lambda x: menu[x])
    return " ".join(res)


# Use .count() then extend by the count
def get_order1(order):
    menu_order = [
        "Burger",
        "Fries",
        "Chicken",
        "Pizza",
        "Sandwich",
        "Onionrings",
        "Milkshake",
        "Coke",
    ]
    clean_order = []

    for item in menu_order:

        count = order.count(item.lower())
        clean_order.extend([item] * count)

    return " ".join(clean_order)
