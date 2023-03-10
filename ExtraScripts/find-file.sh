#!/bin/bash

n_files=0
file_fetched="$1"

found_files=()

function dfs() {
  local path="$1"
  for file in "$path"/*; do
    if [ -d "$file" ]; then
      dfs "$file"
    elif [ "$file" = "$path/$file_fetched" ]; then
      (( n_files++ ))
      found_files+=("$path/$file_fetched")
    fi
  done
}

dfs "/"

if [ ${#found_files[@]} -ne 1 ]; then
  echo "Found $n_files matches"
else
  echo "Found 1 match"
fi

if [ ${#found_files[@]} -gt 0 ]; then
  for file_r in "$found_files"; do
    echo "$file_r"
  done
fi
