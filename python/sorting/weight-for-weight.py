# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python


# Initial Approach
def order_weight(strng):
    if not strng:
        return ""
    weight_list = strng.split()

    # Build matching list of weight digit sums
    totals = []
    for weight in weight_list:
        totals.append(sum(int(d) for d in weight))
    # Zip together
    combined = zip(weight_list, totals)
    # Sort them by the sums, then the original list to handle dupes
    sorted_combined = sorted(combined, key=lambda x: (x[1], x[0]))

    return " ".join([s[0] for s in sorted_combined])


def order_weight2(strng):
    if not strng:
        return ""
    weights = strng.split()

    # Helper function to use as sort key
    def get_weight(w):
        digit_sum = sum(int(d) for d in w)
        return (digit_sum, w)

    # Sort original list by sums, then weights
    weights.sort(key=get_weight)

    return " ".join(weights)
