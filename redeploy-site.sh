#!/bin/sh

WD=$PWD

cd /root/Projects/MLH-project-vitrina-portfolio

git fetch
git reset origin/main --hard

docker compose -f docker-compose.prod.yaml down --rmi all
docker compose -f docker-compose.prod.yaml up -d

cd $WD
