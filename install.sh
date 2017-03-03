#!/bin/bash

# Should run this script to install program in your system.

# Make bdorm directory if it was not in home.
if [ ! -d ~/bdorm ]
then
    mkdir -p ~/bdorm
fi

# Copy files in ~/bdorm.
cp account.db DB.py index.py README.md requirements.txt ~/bdorm
cd ~/bdorm

touch db.py

# Set main address instead of account.db .
sed "s:account.db:$PWD/account.db:" DB.py > db.py
mv index.py bdorm.py
chmod +x bdorm.py

# Remove extra files.
rm DB.py

exit
