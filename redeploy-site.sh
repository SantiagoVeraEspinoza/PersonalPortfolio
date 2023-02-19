#!/bin/sh

tmux kill-server

cd /root/Projects/MLH-project-vitrina-portfolio

git fetch
git reset origin/main --hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt
deactivate

tmux new-session -d -s website_running
tmux send-keys "cd /root/Projects/MLH-project-vitrina-portfolio" C-m
tmux send-keys "source python3-virtualenv/bin/activate" C-m
tmux send-keys "flask run --host=0.0.0.0" C-m