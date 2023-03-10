#!/bin/sh

awk '{print $9}' apache_access | sort | uniq -c | awk '{print $2, $1}' | sort -k1n
[root@santiagoveraespinoza Scripts]# cat get-volume.sh
curl https://cryptingup.com/api/markets | jq -r '.markets |= sort_by(-.volume_24h) | .markets[0:10] | map("\(.symbol) \(.price)") | join("\n")'
[root@santiagoveraespinoza Scripts]# cat problematic-script.sh
#!/usr/bin/env bash

n=$(( RANDOM % 100 ))
if [[ n -eq 42 ]]; then
  echo "Something went wrong"
  >&2 echo "The error was using magic numbers"
  exit 1
fi

echo "Everything went according to plan"
