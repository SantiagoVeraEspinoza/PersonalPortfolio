#!/bin/bash

count=$(awk '{print $1}' apache_access | sort | uniq | wc -l)

echo "Number of source IP addresses: $count"
