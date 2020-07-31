# Raspberry Pi Setup

## Image
1. Use Pi Imager
2. Erase and format sd as FAT32
3. Write Raspian 32 bit
4. `touch ssh`, in boot partition

## Setup
### Ubuntu
Allow internet connection sharing
1. In terminal, `nm-connection-editor`
2. Wired Connection 1, IPv4 settings, Method: “Share with other computers”
Allow network discovery via hostname
3. `sudo apt-get install avahi-daemon`
SSH
4. In terminal, `ssh pi@raspberrypi.local`, password is `raspberry`

### Windows
Allow internet connection sharing
1. Start, Network Connections, Change Adapter Options
2. Wi-fi, Properties, Sharing, Check both boxes
Allow network discovery via hostname
3. Install Bonjour Printing Services from Apple, to detect devices via hostname
4. Directly connect to Pi via ethernet cable
SSH
5. Open Putty
6. Hostname `raspberrypi.local`, port 22, open
7. If this doesn't work:
a. Plug in keyboard & boot Pi
b. Wait a minute, type `pi`, Enter, `raspberry` enter

c. Type `sudo /etc/init.d/ssh start`
d. Type `raspberry`, enter
e. Try Putty again

## Config
1. `sudo adduser your_username`
2. `sudo adduser your_username sudo`
3. `su your_username`
4. `sudo su`, if successful, `exit`
5. `sudo passwd --lock pi`, unlock using `sudo passwd pi`

## raspi-config
1. `sudo raspi-config`
2. Change hostname
3. Enable camera, ssh, vnc
4. Resolution mode 82
5. Boot B1 Desktop / CLI -> Desktop B3
6. Change to Eastern timezone
7. Set WAN to US
8. Resolution mode 82
9. Reboot

## Internet functionality
1. Connect to Wifi
2. `sudo ping -c 5 www.google.com`, check connection

### VNC Cloud, for display view outside LAN
1. On computer install VNC Viewer & make an account
2. Set-up new connection (must still be connected via ethernet)
3. File, New Connection, type hostname.local
4. On pi, click VNC icon in the upper right hand corner, hamburger menu, then license, and sign in
5. At the top of the window view toolbar, select the settings and set picture quality to high
6. Desktop, preferences, screen configuration, configure, HDMI-1, Resolution, 1920x1080
7. Desktop, preferences, appearance settings, Defaults, for large screens

###Update
1. `sudo apt-get update`
2. `sudo apt-get dist-upgrade`

# Install some packages

### Uncomplicated Firewall
1. `sudo apt install ufw`
2. `sudo ufw allow 80`, if you want web hosting
3. `sudo ufw allow ssh`
4. `sudo ufw allow vnc`
5. `sudo ufw enable`, ufw now enabled on startup
6. `sudo ufw status verbose`

### Fail2Ban
Jails IP address that try to brute force password
1. `sudo apt install fail2ban`, enabled by default

### Basic tools
1. `sudo apt install vim`
2. `sudo apt install tmux`
3. `sudo apt install eog`, eye of gnome for X graphical preview
4. `sudo apt install neofetch`

### Camera
1. `sudo usermod -a -G video jonathan`, to give user permission to use camera device
2. `sudo apt install -y gpac`, conversion tool for .h264 video to .mp4 for raspivid

## Python

### Virtualenv
Use python virtual environments to isolate packages
1. `pip3 install virtualenv`
2. `source env/bin/activate`, to activate venv
3. `deactivate`, to deactivate venv

### Dependencies
2. `sudo apt-get install libatlas-base-dev`
3. `sudo apt install libatlas3-base libwebp6 libtiff5 libjasper1 libilmbase23 libopenexr23 libavcodec58 libavformat58 libavutil56 libswscale5 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libatk1.0-0 libcairo-gobject2 libcairo2 libgdk-pixbuf2.0-0 libqtgui4 libqt4-test libqtcore4`
4. `pip3 install opencv-python==3.4.6.27`, latest version doesn’t work well with Pi
