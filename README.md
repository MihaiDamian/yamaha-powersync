yamaha-powersync
================


A simple script you can use to power on/off your receiver when your computer start/shuts down. Works with most network-enabled Yamaha® AV receivers. Tested on Yamaha RX-V475.


Basic usage instructions
------------------------

Open `yamaha-powersync.py` and replace the IP in `HOSTNAME` with your receivers' IP address. Make sure you've previously assigned a static IP for the receiver.

To power on your receiver:

    python yamaha-powersync.py start
    
To power off your receiver:

    python yamaha-powersync.py stop
    
    
Scheduling the script to be executed on startup/shutdown
--------------------------------------------------------

This step depends on your OS. If you're using Windows 8 you can use `gpedit` to execute scripts at startup/shutdown. The place to configure this is `Local Computer Policy/Computer Configuration/Windows Settings/Scripts (Startup/Shutdown)`
