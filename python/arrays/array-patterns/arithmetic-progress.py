def find_missing(sequence):
    # Formula to find step between numbers
    step = (sequence[-1] - sequence[0]) // len(sequence)
    # Stop before last index to avoid error
    for i in range(len(sequence) - 1):
        # If num ahead != num + step, return what it should be
        if sequence[i + 1] != sequence[i] + step:
            return sequence[i] + step
