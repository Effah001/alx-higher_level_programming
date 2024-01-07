#!/usr/bin/python3

"""get error message"""

import sys
import urllib.request
import urllib.error


def main():
    url = sys.argv[1]
    reqst = urllib.request.Request(url)

    try:
        with response = urllib.request.urlopen(reqst)
        print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
