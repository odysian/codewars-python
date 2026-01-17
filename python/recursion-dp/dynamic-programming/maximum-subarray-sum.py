# Kadane's Algorithm
def max_sequence(arr):
    current_sum = 0
    max_sum = 0
    for x in arr:
        # Add each num to current sum
        current_sum += x
        # If current sum is negative, drop it, start over
        if current_sum < 0:
            current_sum = 0
        # Keep highest score as we go
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
