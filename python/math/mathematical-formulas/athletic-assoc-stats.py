# https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python


# Refactored
def stat(strg):
    if not strg:
        return ""

    def to_seconds(time_str):
        h, m, s = map(int, time_str.split("|"))
        return h * 3600 + m * 60 + s

    def to_time_format(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02d}|{m:02d}|{s:02d}"

    times = sorted([to_seconds(s.strip()) for s in strg.split(",")])
    range_val = times[-1] - times[0]
    mean = sum(times) // len(times)

    mid = len(times) // 2
    if len(times) % 2 == 0:
        median = (times[mid - 1] + times[mid]) // 2
    else:
        median = times[mid]

    return (
        f"Range: {to_time_format(range_val)} "
        f"Average: {to_time_format(mean)} "
        f"Median: {to_time_format(median)}"
    )


# Original
def stat1(strg):
    if not strg:
        return ""

    def encode_time(time_str):
        cleaned = time_str.split("|")
        out = 0
        out += int(cleaned[0]) * 3600
        out += int(cleaned[1]) * 60
        out += int(cleaned[2])
        return out

    def decode_time(time_int):
        out = []
        hours = time_int // 3600
        time_int = time_int % 3600
        out.append(str(hours).zfill(2))

        minutes = time_int // 60
        time_int = time_int % 60
        out.append(str(minutes).zfill(2))

        seconds = time_int
        out.append(str(seconds).zfill(2))
        joined = "|".join(out)
        return joined

    encode_time("01|15|59")
    decode_time(4559)

    values = [encode_time(s) for s in strg.split(",")]
    values.sort()
    leng = len(values)
    mid = values[leng // 2]
    mean = int(sum(values) // len(values))
    if len(values) % 2 == 0:
        median = int((mid + values[(leng // 2) - 1]) / 2)
    else:
        median = int(mid)
    range = int(max(values) - min(values))
    out = [range, mean, median]

    output = [decode_time(o) for o in out]
    return f"Range: {output[0]} Average: {output[1]} Median: {output[2]}"
