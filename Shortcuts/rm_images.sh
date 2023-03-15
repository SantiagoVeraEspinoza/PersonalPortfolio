#!/bin/bash

docker stop mysql
docker stop myportfolio

docker rm mysql
docker rm myportfolio

docker rmi mariadb
docker rmi mlh-project-vitrina-portfolio-myportfolio