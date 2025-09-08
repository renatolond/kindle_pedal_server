#!/bin/sh

KH_HACKNAME="wifi_pedal_server"
# Pull default helper functions for logging
_FUNCTIONS=/etc/rc.d/functions
. ${_FUNCTIONS}

iptables -A INPUT -i wlan0 -p tcp --dport 8000 -j ACCEPT
nohup python3 "/mnt/us/extensions/${KH_HACKNAME}/bin/server.py" &
msg "Server started"
