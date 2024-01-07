#!/usr/bin/python3

"""Get email"""

import urllib.parse
import urllib.request
import sys


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode("utf-8")

    with urllib.request.urlopen(url, data=data) as response:
        result = response.read().decode("utf-8")
        print(result)


if __name__ == "__main__":
    main()
