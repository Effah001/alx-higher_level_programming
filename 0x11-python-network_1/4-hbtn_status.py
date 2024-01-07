#!/usr/bin/python3
"""Get status"""
import requests


def main():
    content = requests.get('https://alx-intranet.hbtn.io/status')
    html = content.text
        print("Body response:\n\t- type:", type(html.decode('utf-8')))
        print("\t- content:", html.decode('utf-8'))


if __name__ == "__main__":
    main()
