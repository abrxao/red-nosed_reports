import numpy as np

# Fullname: Abraão de Carvalho Albuquerque


def read_input_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines in data.txt files
    # I decided to use python, because I saw that the numbers of values in each
    # line was different and python array can handle this problem easily
    data = [list(map(int, line.strip().split())) for line in lines]
    return data


def is_safe(report):
    # This method get diff of each pair (index, index+1) of one line of the "matrix"
    # returned in read_input_line()
    diffs = np.diff(report)

    if np.all(diffs > 0):  # Verify if all diff in one line are increasing
        # Verify if the range of diffs is correct (1<=diff<=3)
        return np.all((diffs >= 1) & (diffs <= 3))
    elif np.all(diffs < 0):  # Verify if  all diff in one line are decreasing
        # Verify if the range of diffs is correct (-3<=diff<=-1)
        return np.all((diffs <= -1) & (diffs >= -3))
    else:
        # Return false if none of the criteria was satisfied
        return False


def count_safe_reports(reports):
    # Function that check all lines of "data.txt" file
    # Created just to be more easy to read this code
    safe_count = sum(1 for report in reports if is_safe(report))
    return safe_count


if __name__ == "__main__":
    # Get the "matrix"
    reports = read_input_line("data.txt")
    # Make the count
    safe_reports_count = count_safe_reports(reports)
    print(f"Number of safe reports: {safe_reports_count}")

    # Number of safe reports: 631
