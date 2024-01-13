#!/bin/bash
# Bash script that sends a JSON POST request to a URL and displays the body
url="$1"; filename="$2"; curl -s -X POST -H "Content-Type: application/json" -d "@$filename" "$url"
