from network_manager import NetworkManager
from pimoroni import Button, PWMLED
import uasyncio
import urequests
import time


# Fill up the following vars with whatever you would like
WIFI_COUNTRY = ""
WIFI_SSID = ""
WIFI_PASSWORD = ""
WIFI_CHANNEL = -1

SERVER_IP = "http://192.168.4.16:8000"
FORWARD_ADDRESS = "{}/forward".format(SERVER_IP)
BACKWARD_ADDRESS = "{}/backward".format(SERVER_IP)

# set up the buttons, change according to your wiring
FORWARD_BUTTON_PIN = 14
BACKWARD_BUTTON_PIN = 10

LED_PIN = 1
LED_BLINK_TIME = 0.2

forward_button = Button(FORWARD_BUTTON_PIN, invert=True)
backward_button = Button(BACKWARD_BUTTON_PIN, invert=True)

activity_led = PWMLED(LED_PIN)
activity_led.off()

def status_handler(mode, status, ip):
    status_text = "Creating AP..."
    print(status_text)
    if status is not None:
        if status:
            status_text = "SUCCESS! {}".format(ip)
        else:
            status_text = "Failed! {}".format(status)
    print(status_text)

# Set up AP
network_manager = NetworkManager(WIFI_COUNTRY, status_handler=status_handler)

# connect to wifi
event_loop = uasyncio.get_event_loop()
event_loop.run_until_complete(network_manager.access_point(WIFI_SSID, WIFI_CHANNEL, WIFI_PASSWORD))

while True:
   if forward_button.is_pressed:
     activity_led.on()
     r = urequests.get(FORWARD_ADDRESS)
     r.close()
     time.sleep(LED_BLINK_TIME)
     activity_led.off()
   if backward_button.is_pressed:
     activity_led.on()
     r = urequests.get(BACKWARD_ADDRESS)
     r.close()
     time.sleep(LED_BLINK_TIME)
     activity_led.off()
