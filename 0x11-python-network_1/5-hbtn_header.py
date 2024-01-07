#!/usr/bin/python3

"""display X-request-Id"""
import requests
import sys


def main():
    url = sys.argv[1]

    content = requests.get(url)
    x_request_id = content.headers.get('X-Request-Id')

    print(x_request_id)


if __name__ == "__main__":
    main()
