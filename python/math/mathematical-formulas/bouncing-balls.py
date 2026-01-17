def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    rebound = h * bounce
    count = 1

    while rebound > window:
        count += 2
        rebound = rebound * bounce

    return count
