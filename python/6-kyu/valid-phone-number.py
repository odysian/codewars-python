def valid_phone_number(phone_number):
    if len(phone_number) != 14:
        return False
    # Check the skeleton
    if not (
        phone_number[0] == "("
        and phone_number[4] == ")"
        and phone_number[5] == " "
        and phone_number[9] == "-"
    ):
        return False
    # Slice into parts
    parts = [phone_number[1:4], phone_number[6:9], phone_number[10:14]]
    # Check parts are all digits
    return all(part.isdigit() for part in parts)
