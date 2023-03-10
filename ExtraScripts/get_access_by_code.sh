#!/bin/sh

awk '{print $9}' apache_access | sort | uniq -c | awk '{print $2, $1}' | sort -k1n
