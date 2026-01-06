# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python


def pick_peaks(arr):
    # Init dict with pos and peaks keys
    res = {}
    res["pos"] = []
    res["peaks"] = []
    # Two pointers to scan for peaks and plateaus
    l = 1
    r = 2
    # Keep r in bounds
    while r < len(arr):
        # If l is possible peak/start of plateau
        if arr[l] > arr[l - 1]:
            # Scan ahead
            if arr[l] == arr[r]:
                r += 1
                continue
            # If r goes down, we found a peak/plateau
            if arr[l] > arr[r]:
                res["pos"].append(l)
                res["peaks"].append(arr[l])
            # Snap l to r and move ahead
            l = r
            r += 1
        # If no possible peak found, move on
        else:
            l += 1
            r += 1
    return res
