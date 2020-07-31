## Flash microSD
1. Download Raspberry Pi Imager
2. Erase and format microSD with FAT32
3. Write drive with 32 bit default Raspian
4. Add `ssh` file to boot directory, no extension

Allow Internet Connection Sharing
    Plug in Pi directly to computer via ethernet
Windows
Right click Start, Network Connections, Change Adapter Options
Right click Wi-fi, Properties, Sharing, Check both boxes
Ubuntu
Terminal: nm-connection-editor
Double click Wired Connection 1, IPv4 settings, Method: “Share with other computers”
Boot up Pi
Plug Pi to laptop via ethernet, insert microSD, and power on
SSH into Pi
    Allow network discovery via hostname using Avahi on Linux or Bonjour on Windows instead of having to find ip address of pi
Windows
Install Bonjour Printing Services from Apple (used to detect devices)
Open Putty
Type raspberrypi.local into Hostname, port 22, click open
If you can’t connect (guide)
Plug in keyboard & boot Pi
Wait a minute, type pi, Enter, raspberry enter
Then type sudo /etc/init.d/ssh start
Then type raspberry and hit enter
Try Putty again
Ubuntu
sudo apt-get install avahi-daemon
Open terminal, ssh pi@raspberrypi.local
Configure Raspi
Login as: pi
Password: raspberry
Sudo raspi-config
Complete the following steps:
Option 1: Change password
Option 2: Change hostname → research
Option 3: B1 Desktop / CLI → B3 Desktop
Option 5: Enable ssh and vnc
Option 7: Resolution → Mode 82
Finish & reboot
End session
Get ip address using Hostname -I 
Set-up VNC
Install VNC Viewer & make an account
Set-up new connection (must still be connected via ethernet)
File, New Connection, type ip address
Complete set-up pop-up
Skip wifi & update, restart later
Check internet
Open terminal (ctrl alt t) and type sudo ping -c 5 www.google.com
If ping goes through, then you have internet
Else, try turning on laptop mobile hotspot to connect wirelessly
Set-up VNC Cloud
        Allow access outside LAN
Click VNC icon in the upper right hand corner, hamburger menu, then license, and sign in
In the top toolbar, select the settings and set picture quality to high
In the desktop, preferences, screen configuration, configure, HDMI-1, Resolution, 1920x1080
Desktop, preferences, appearance settings, Defaults, for large screens
Create new user
sudo adduser jonathan
sudo adduser jonathan sudo
su jonathan
sudo su
If successful type exit
sudo passwd --lock pi
Type sudo passwd pi to unlock pi password
Update Raspian
sudo apt-get update
sudo apt-get dist-upgrade
Uncomplicated Firewall (Official documentation, ufw guide)
sudo apt install ufw
sudo ufw allow 80
Allows incoming connection on port 80 for website hosting
sudo ufw allow ssh
Sudo ufw allow 25565
Sudo ufw allow vnc
sudo ufw enable (firewall is now enabled on start-up)
Default allows all outgoing and blocks all incoming
sudo ufw status verbose
Displays your ufw rules
Install Fail2ban (Official documentation)
Protects from brute force attempts by blocking IP addresses that enter password wrong too many times
sudo apt install fail2ban
It is enabled by default

Research Setup
Basics
sudo apt update
sudo apt install git vim tmux
Python
pip3 install virtualenv
source env/bin/activate
pip3 install opencv-python==3.4.6.27 (latest version doesn’t work well with Pi)
deactivate
