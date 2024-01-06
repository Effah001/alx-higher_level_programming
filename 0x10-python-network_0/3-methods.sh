#!/bin/bash
# Display all HTTP allowed on the server
curl -sI $@ | grep 'Allow' | sed 's/Allow: //'
