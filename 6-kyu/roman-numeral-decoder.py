def solution(roman: str) -> int:
    # Use dict for string matching
    values = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }
    total = 0
    idx = 0

    while idx < len(roman):
        # If not last index and two char numeral in dict
        if idx + 1 < len(roman) and roman[idx : idx + 2] in values:
            total += values[roman[idx : idx + 2]]
            idx += 2
            continue
        # Else add matching single char or last char
        else:
            total += values[roman[idx]]
            idx += 1

    return total
