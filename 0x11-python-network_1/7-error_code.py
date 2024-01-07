#!/usr/bin/python3

"""get error message"""

import sys
import requests


def main():
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")


if __name__ == "__main__":
    main()
