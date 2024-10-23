#!/usr/bin/python3
"""Reads from standard input and computes metrics"""

import re
import sys


def extract_input(line):
    """Extracts input from standard input.
    Args:
        line (str): Input from standard input
    """
    regex = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )

    info = {
        'status_code': '0',
        'file_size': 0,
    }

    fmt = '{}\\-{}{}{}{}\\s*'.format(regex[0], regex[1],
                                     regex[2], regex[3], regex[4])
    match = re.fullmatch(fmt, line)
    if match is not None:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size

    return info


def print_metrics(size, status_codes):
    """Print metrics.

    Args:
        size (int): the accumulated read file size.
        status_codes (dict): the accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0
    try:
        for line in sys.stdin:
            if count == 10:
                print_metrics(size, status_codes)
                count = 1
            else:
                count += 1
            info = extract_input(line)
            file_size = info.get('file_size', '0')
            status_code = info.get('status_code', '0')
            try:
                if status_code in valid_codes:
                    if status_codes.get(status_code, -1) == -1:
                        status_codes[status_code] = 1
                    else:
                        status_codes[status_code] += 1
                    size += int(file_size)
            except (IndexError, ValueError):
                pass
    except (KeyboardInterrupt, EOFError):
        print_metrics(size, status_codes)
        raise
