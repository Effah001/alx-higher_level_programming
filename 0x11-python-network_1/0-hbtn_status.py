#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read().decode('utf-8')
print("Body response:")
print("    - type:", type(html))
print("    - content:", html)
print("    - utf8 content:", html)
