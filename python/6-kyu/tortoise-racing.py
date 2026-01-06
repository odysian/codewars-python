def race(v1, v2, g):
    if v1 > v2:
        return None

    # ALWAYS CONVERT TO SMALLEST UNIT
    time_seconds = (g * 3600) // (v2 - v1)

    hours = time_seconds // 3600
    minutes = (time_seconds % 3600) // 60
    seconds = time_seconds % 60

    return [hours, minutes, seconds]
