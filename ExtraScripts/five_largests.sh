#!/bin/sh

awk '{print $NF, $0}' apache_access | sort -nr | head -5 | cut -d" " -f2-
