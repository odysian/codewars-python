def meeting(s):
    people = s.upper().split(";")

    cleaned = []
    for person in people:
        first, last = person.split(":")
        cleaned.append((last, first))

    cleaned.sort()
    return "".join(f"({last}, {first})" for last, first in cleaned)
