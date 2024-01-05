#!/bin/bash
#Get all the methods from the server
curl -sI -X OPTIONS "$1" | grep -i allow | awk '{print $2}'

