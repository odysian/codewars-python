# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python


def longest_palindrome(s):
    if not s:
        return 0

    longest = 0

    # Loop through every possible starting index
    for i in range(len(s)):

        # For odd len strings, start at same index
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current_len = r - l + 1
            longest = max(longest, current_len)
            l -= 1
            r += 1

        # For even, start apart
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current_len = r - l + 1
            longest = max(longest, current_len)
            l -= 1
            r += 1

    return longest
