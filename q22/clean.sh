#!/bin/bash

FILE1=$1
tr , '\n' < names.txt | sed 's/,//g' | sed 's/"//g' | sort | awk '{print NR, $0}' > final.txt

