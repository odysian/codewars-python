def queue_time(customers, n):
    # Create list of tills
    tills = [0] * n

    for c in customers:
        # Find lowest value till(one that is open)
        min_value = min(tills)
        min_index = tills.index(min_value)

        # Add customer time to that till
        tills[min_index] += c

    # Return when last till finishes
    return max(tills)
