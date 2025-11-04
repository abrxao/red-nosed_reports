import numpy as np


def read_input_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    data = [list(map(int, line.strip().split())) for line in lines]
    return data


def is_safe(report):
    diffs = np.diff(report)

    if np.all(diffs > 0):
        return np.all((diffs >= 1) & (diffs <= 3))
    elif np.all(diffs < 0):
        return np.all((diffs <= -1) & (diffs >= -3))
    else:
        return False


def count_safe_reports(reports):
    safe_count = sum(1 for report in reports if is_safe(report))
    return safe_count


if __name__ == "__main__":
    reports = read_input_line("data.txt")
    safe_reports_count = count_safe_reports(reports)
    print(f"Number of safe reports: {safe_reports_count}")
