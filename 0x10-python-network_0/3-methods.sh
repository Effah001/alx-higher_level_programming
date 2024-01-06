#!/bin/bash
# Display all HTTP allowed on the server
curl -si -L -X OPTIONS $@| grep 'Allow:' | awk '{print $2}'
