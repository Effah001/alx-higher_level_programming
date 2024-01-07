#!/usr/bin/python3
"""Get status"""
import urllib.request


def main():
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        html = resp.read()
        print("Body response:\n\t- type:", type(html.decode('utf-8')))
        print("\t- content:", html.decode('utf-8'))


if __name__ == "__main__":
    main()
