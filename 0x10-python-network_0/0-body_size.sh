#!/bin/bash
size=$(curl -s -w '%{size_download}' -o /dev/null https://www.example.com)
echo -e "$size"
