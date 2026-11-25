"""Convert a 12-hour time string to 24-hour time."""


def timeConversion(s):
    """Return the 24-hour representation of a time ending in AM or PM."""
    period = s[-2:]
    hour = int(s[:2])

    if period == "AM":
        hour = 0 if hour == 12 else hour
    elif hour != 12:
        hour += 12

    return f"{hour:02d}{s[2:8]}"


if __name__ == "__main__":
    import sys

    time_string = sys.stdin.readline().strip()
    if not time_string:
        raise SystemExit("Please enter a time such as 07:05:45PM.")

    print(timeConversion(time_string))
