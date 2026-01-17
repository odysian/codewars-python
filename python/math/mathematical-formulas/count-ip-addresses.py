# https://www.codewars.com/kata/526989a41034285187000de4/train/python


def ips_between(start, end):
    # Func to convert an ip address to total possible addresses
    def ip_to_number(ip):
        parts = ip.split(".")
        total = 0
        # Use base 256 to calc each octet
        for i, part in enumerate(parts):
            power = 3 - i
            total += int(part) * (256**power)
        return total

    start_num = ip_to_number(start)
    end_num = ip_to_number(end)
    # Subtract to find addresses in range
    return end_num - start_num
