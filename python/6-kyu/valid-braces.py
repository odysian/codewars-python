def valid_braces(string):
    # Dict to match closing bracket as key
    braces = {")": "(", "}": "{", "]": "["}

    stack = []
    for char in string:
        # If closing bracket
        if char in braces:
            # If stack empty or top of stack != matching opening bracket
            if not stack or stack[-1] != braces[char]:
                return False
            # Pop if it matches
            stack.pop()
        # Append opening brackets
        else:
            stack.append(char)

    return not stack
