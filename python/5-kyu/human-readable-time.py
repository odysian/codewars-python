# Clean Math Approach
def make_readable(seconds):
    hours = seconds // 3600
    remainder = seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def make_readable2(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
