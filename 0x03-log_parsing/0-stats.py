#!/usr/bin/python3

import sys
import re


def compute_metrics(lines):
    total_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0,
                          401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    for line in lines:
        match = re.match(
            r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" \d+ (\d+)$', line.strip())
        if not match:
            continue

        file_size = int(match.group(1))
        total_size += file_size

        status_code = int(line.split()[8])
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    return total_size, status_code_counts


def print_statistics(total_size, status_code_counts):
    print(f"Total file size: {total_size}")
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")


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
