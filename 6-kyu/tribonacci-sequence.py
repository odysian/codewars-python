def tribonacci(signature, n):
    if n == 0:
        return []

    result = signature[:]

    while len(result) < n:
        result.append(sum(result[-3:]))

    return result[:n]
