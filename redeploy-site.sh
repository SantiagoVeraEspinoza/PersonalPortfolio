#!/bin/sh

WD=$PWD

cd /root/Projects/PersonalPortfolio

git fetch
git reset origin/main --hard

docker compose -f docker-compose.prod.yaml down
docker compose -f docker-compose.prod.yaml up -d --build
docker system prune

cd $WD
