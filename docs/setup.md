# Raspberry Pi Setup
This walks through how to set up Sparcfire on a Raspberry Pi 4. This requires a microSD card, microSD-to-USB adapter, and an Ethernet cable.

## 1. Raspian Image
1. Use Pi Imager
2. Erase and format sd as FAT32
3. Write Raspian 32 bit
4. `$ touch ssh`, in boot partition

## 2. Connect via SSH
Plug in the microSD card and power on the Pi. Connect the Pi to your computer via an Ethernet cable. Before SSHing, we need to setup internet connection sharing and allow network discovery via hostname.

### For Ubuntu
1. `$ nm-connection-editor`
2. Select Wired Connection 1, IPv4 settings, Method: “Share with other computers”
3. `$ sudo apt-get install avahi-daemon`
4. `$ ssh pi@raspberrypi.local`, password: `raspberry`

### For Windows
1. Select Start, Network Connections, Change Adapter Options
2. Then Wi-fi, Properties, Sharing, and check both boxes
3. Install Bonjour Printing Services, this allows your compter to detect devices via hostname
4. Open Putty
5. Enter Hostname: `raspberrypi.local`, port 22, and open

### Debugging SSH
Try these instructions if you get a `ssh: Could not resolve hostname` error
1. Boot the Pi and plug in a USB keyboard
2. Wait a minute for the Pi to boot
3. In the keyboard type `pi`, enter, `raspberry`, enter
4. Type `sudo /etc/init.d/ssh start`
5. Type `raspberry`, enter
6. Now try SSHing again

## 3. Basic Configuration
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

### VNC Cloud
Set this up for desktop display view over Internet
1. On computer install VNC Viewer & make an account
2. Set-up new connection (must still be connected via ethernet)
3. File, New Connection, type hostname.local
4. On pi, click VNC icon in the upper right hand corner, hamburger menu, then license, and sign in
5. At the top of the window view toolbar, select the settings and set picture quality to high
6. Desktop, preferences, screen configuration, configure, HDMI-1, Resolution, 1920x1080
7. Desktop, preferences, appearance settings, Defaults, for large screens

### Update
1. `sudo apt-get update`
2. `sudo apt-get dist-upgrade`

# 4. Installation

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
1. `sudo usermod -a -G video user_name`, to give user permission to use camera device
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

### Setting up LED strip
https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/
1. `sudo apt-get update
2. `sudo apt-get install scons swig`
3. `sudo vim /etc/modprobe.d/snd-blacklist.conf`, add the following line, `blacklist snd_bcm2835`
4. `sudo vim /boot/config.txt`, comment out `#dtparam=audio=on`
5. `sudo reboot`


# History dump from LED strip

sudo apt-get update
sudo apt-get install gcc make build-essential
sudo apt-get install python-dev
sudo apt get install scons
sudo apt-get install scons
sudo apt-get install swig
sudo vim /etc/modprobe.d/snd-blacklist.conf
sudo vim /boot/config.txt
sudo reboot

git clone https://github.com/jgarff/rpi_ws281x
cd rpi_ws281x/
sudo scons
sudo python setup.py build
sudo python setup.py install

sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/strandtest.py

sudo python3 setup.py build
sudo python3 setup.py install
sudo pip3 install rpi_ws281x
sudo python3 test.py -c

pip3 list --local
pip list --local

sudo pip uninstall rpi-ws281x
pip freeze > requirements.txt
cat requirements.txt 

chmod -x testpasswd.sh
./testpasswd.sh
ls
chmod -x testpasswd.sh
./testpasswd.sh
ls -l
bash testpasswd.sh 
vim testpasswd.sh 
bash testpasswd.sh 
ls -l
cd ..
chmod -x install/testpasswd.sh 
chmod 755 testpasswd.sh
