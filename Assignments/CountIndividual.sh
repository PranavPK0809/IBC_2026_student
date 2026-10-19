#!/usr/bin/bash

# Count the number of samples for an individual
# $1 is the data file and $2 is the individual ID

cut -f 1 $1 | grep -w -c $2