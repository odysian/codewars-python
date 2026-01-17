def count_smileys(arr):

    # Use sets for membership checks
    eyes = {":", ";"}
    nose = {"-", "~"}
    mouth = {")", "D"}
    count = 0

    for face in arr:
        # Rule out eyes first
        if face[0] not in eyes:
            continue

        # Check lengths and then handle nose + mouth
        if len(face) == 2 and face[1] in mouth:
            count += 1
        elif len(face) == 3 and face[1] in nose and face[2] in mouth:
            count += 1

    return count
