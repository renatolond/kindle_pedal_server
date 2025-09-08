from network_manager import NetworkManager
from pimoroni import RGBLED, Button
import uasyncio
import urequests

# Fill up the following vars with whatever you would like
WIFI_COUNTRY = ""
WIFI_SSID = ""
WIFI_PASSWORD = ""
WIFI_CHANNEL = -1

SERVER_IP = "http://192.168.4.16:8000"
FORWARD_ADDRESS = "{}/forward".format(SERVER_IP)
BACKWARD_ADDRESS = "{}/backward".format(SERVER_IP)

# set up the buttons, change according to your wiring
button_a = Button(12, invert=True)
button_b = Button(13, invert=True)

def status_handler(mode, status, ip):
    status_text = "Creating AP..."
    if status is not None:
        if status:
            status_text = "SUCCESS! {}".format(status)
        else:
            status_text = "Failed! {}".format(status)

# Set up AP
network_manager = NetworkManager("be", status_handler=status_handler)
network_manager.disconnect()

# connect to wifi
event_loop = uasyncio.get_event_loop()
event_loop.run_until_complete(network_manager.access_point(WIFI_SSID, WIFI_CHANNEL, WIFI_PASSWORD))

while True:
   if button_a.is_pressed:
     r = urequests.get(FORWARD_ADDRESS)
     r.close()
   if button_b.is_pressed:
     r = urequests.get(BACKWARD_ADDRESS)
     r.close()


