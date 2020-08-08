#!/bin/bash

user=sparcfire
match=false
while [ "$match" = false ]
do
	#create user here
	read -s -p "Enter password: " passwd1
	echo ""
	read -s -p "Enter password again: " passwd2
	if [[ "$passwd1" == "$passwd2" ]]
	then
		match=true	
	fi
done
echo -e "\ndone"
