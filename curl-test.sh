#!/bin/bash

name=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)
email=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)"@"$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)".com"
content=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)

curl --request POST http://127.0.0.1:5000/api/timeline_post -d "name=$name&email=$email&content=$content"

curl http://127.0.0.1:5000/api/timeline_post | grep "$name" | grep "$email" | grep "$content"
