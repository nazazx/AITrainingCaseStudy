# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.


def average_valid_measurements(values):

    if not isinstance(values, (list, tuple)):
        return None

    total = 0
    count = 0

    for v in values:
        if v is None:
            continue

        try:
            num = float(v)
        except (TypeError,ValueError):
            continue

        total += num
        count += 1

    if count == 0:
        return None

    return total / count