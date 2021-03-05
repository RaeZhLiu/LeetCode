#!/bin/bash

fileName=$1
cat "${fileName}" | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'