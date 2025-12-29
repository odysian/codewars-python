def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""

    counts = {cat: 0 for cat in categories}

    for listing in stocklist:
        cat = listing[0]
        if cat in categories:
            qty = int(listing.split()[1])
            counts[cat] += qty

    output = [f"({cat} : {counts[cat]})" for cat in categories]
    return " - ".join(output)
