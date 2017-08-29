#!/bin/bash

FILE1=$1
tr , '\n' < words.txt | sed 's/,//g' | sed 's/"//g' | sort | awk '{print $0}' > final.txt

