yamaha-powersync
================


A simple script you can use to power on/off your receiver when your computer start/shuts down.


Requirements
------------
* A network enabled Yamaha® AV receivers (tested on Yamaha RX-V475)
* [Python](http://www.python.org/) 2.7 or later
* The [Requests](http://docs.python-requests.org) library


Basic usage instructions
------------------------

Open `yamaha-powersync.py` and replace the IP in `HOSTNAME` with your receiver's IP address. Make sure you've previously assigned a static IP for the receiver.

To power on your receiver:

    python yamaha-powersync.py start
    
To power off your receiver:

    python yamaha-powersync.py stop
    
    
Scheduling the script to be executed on startup/shutdown
--------------------------------------------------------

This step depends on your OS. If you're using Windows 8 you can use `gpedit` to execute scripts at startup/shutdown. The place to configure this is `Local Computer Policy/Computer Configuration/Windows Settings/Scripts (Startup/Shutdown)`
