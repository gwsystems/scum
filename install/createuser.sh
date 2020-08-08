#!/bin/bash

# Create user named sparcfire
user=sparcfire
echo "Creating new user $user"
adduser $user
adduser $user sudo
echo "Created user $user"


# Lock pi password, use `sudo passwd pi` to unlock
passwd --lock pi


exit

