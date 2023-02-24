#!/bin/sh

WD=$PWD

cd /root/Projects/MLH-project-vitrina-portfolio

git fetch
git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt
deactivate

systemctl daemon-reload
systemctl restart myportfolio

cd $WD
