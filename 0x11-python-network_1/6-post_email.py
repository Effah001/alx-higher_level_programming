#!/usr/bin/python3

"""Get email"""

import requests
import sys


def main():
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    response = requests.post(url, data=data)
    result = response.text
    print(result)


if __name__ == "__main__":
    main()
