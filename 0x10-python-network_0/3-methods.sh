#!/bin/bash
#Get all the methods from the server
response=$(curl -si -X OPTIONS $@); echo "$response";
