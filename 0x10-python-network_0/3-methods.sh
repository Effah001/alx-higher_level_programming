#!/bin/bash
# display all HTTP methods accepted by the server
curl -sI $1 | grep 'Allow' | sed 's/Allow: //'
