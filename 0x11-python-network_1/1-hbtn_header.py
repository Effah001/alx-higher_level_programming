#!/usr/bin/python3

"""display X-request-Id"""
import urllib.request
import sys


def main():
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        header = response.info()

        x_request_id = header.get('X-Request-Id')

        print(x_request_id)


if __name__ == "__main__":
    main()
