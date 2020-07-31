`hcitool scan`, this only lists devices that are in pair mode


# iBeacon scanner, requires BLE dongle to scan iBeacons

https://www.thepolyglotdeveloper.com/2016/09/scan-bluetooth-enabled-ibeacons-via-raspberry-pi-iot-device/

`sudo apt-get install bluez bluez-hcidump`

run
`sudo hcitool lescan --duplicates &`
`sudo hcidump --raw`
