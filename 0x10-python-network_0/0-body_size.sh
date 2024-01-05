#!/bin/bash
#a Bash script that displays the size of the body of the response
size=$(curl -s -w '%{size_download}' -o /dev/null $@); echo -e "$size"
