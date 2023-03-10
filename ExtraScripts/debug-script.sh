#!/bin/bash

script_path="$1"
count=0

while true; do
  ((count++))
  output=$(source "$script_path" 2>&1)
  exit_code=$?
  error_output=$(echo "$output" | tail -n 1)
  output=$(echo "$output" | head -n 1)

  if [ $exit_code -ne 0 ]; then
    echo "It took $count runs to fail."
    echo "Standard Output:"
    echo "$output"
    echo "Standard Error:"
    echo "$error_output"
    break
  fi
done
