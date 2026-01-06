def create_phone_number(n):

    s = [str(i) for i in n]
    area_code = "".join(s[:3])
    first_3 = "".join(s[3:6])
    last_4 = "".join(s[6:10])

    return f"({area_code}) {first_3}-{last_4}"
