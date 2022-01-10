#! /bin/bash

echo "StrictHostKeyChecking no" >> /home/user/.ssh/config
git config --global user.email $gitemail
git config --global user.name $gitusername
python3 consensus.py
