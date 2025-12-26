def digital_root(n):

    # While n is more than one digit
    while n >= 10:

        # Empty list to store digits
        new_nums = []
        # Convert to string to measure length
        string_num = str(n)

        for char in string_num:
            # Add each digit to list
            new_nums.append(int(char))

        # Sum all the digits
        n = sum(new_nums)

    return n
