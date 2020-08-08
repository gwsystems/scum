#!/bin/bash
# To make executable `chmod +x install.sh` or `chmod 755 install.sh` if the prior doesn't work
# run using `./install.sh`

# Variables
user=sparcfire

echo "setting up new user $user"
adduser $user


echo "raspi-config"
echo "updating packages"
echo "installing packages"
echo "preparing python virtualenv"

