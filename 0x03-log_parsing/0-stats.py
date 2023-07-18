#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics"""

import sys


def compute_metrics(lines):
    total_size = 0
    status_code_counts = {}

    for line in lines:
        parts = line.split()
        if len(parts) != 10:
            continue

        try:
            file_size = int(parts[9])
            total_size += file_size

            status_code = int(parts[7])
            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code_counts[status_code] = status_code_counts.get(
                    status_code, 0) + 1
        except ValueError:
            continue

    return total_size, status_code_counts


def print_statistics(total_size, status_code_counts):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")


def main():
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) % 10 == 0:
                total_size, status_code_counts = compute_metrics(lines)
                print_statistics(total_size, status_code_counts)
                lines = []
    except KeyboardInterrupt:
        total_size, status_code_counts = compute_metrics(lines)
        print_statistics(total_size, status_code_counts)


if __name__ == "__main__":
    main()
