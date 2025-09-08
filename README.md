Kindle Pedal Server
====

This repository contains code for a Kindle Pedal Server.

Using a jailbroke kindle, one can install an extension on the kindle to enable a server which receives "page forward" and "page backwards" commands.

To make use of the server, one needs a Raspberry Pi Pico W, which will initialize the wifi in AP mode and receive the button commands to send it to the kindle.

This project is based off [Kindle WiFi Remote Footswitch](https://www.instructables.com/Kindle-WiFi-Remote-Footswitch/). The software part of that project does not seem to work on newer kindles, so I went a different route.

This is tested on a Kindle Paperwhite 11th Gen and only guaranteed to work on this setup.
