# Initial Approach
def increment_string(strng):
    if not strng:
        return "1"
    # Check if num at end, if not return +"1"
    if strng[-1].isalpha():
        return strng + "1"
    # Find index from right side of first nondigit
    idx = 0
    for i, s in enumerate(strng[::-1]):
        if not s.isdigit():
            idx = i * -1
            break
    # Seperate number, store len, add 1, cast str and zfill
    num = strng[idx:]
    num_len = len(num)
    int_num = int(num) + 1
    new_num = str(int_num).zfill(num_len)
    # Put it back together
    return strng[:idx] + new_num


# Improved approach, using rstrip()
def increment_string2(strng):
    # Strip away the number from the right side
    head = strng.rstrip("0123456789")
    # Use len of head to store number we just stripped away
    tail = strng[len(head) :]

    if not tail:
        return strng + "1"
    # Add 1 to number
    number = int(tail) + 1
    # Concat and use zfill to put zeroes back in
    return head + str(number).zfill(len(tail))
