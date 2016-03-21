# HDmx
Simple OSC to DMX interface

What is it
-------------

This is a python program listening OSC on port 3000, and sending command to a DMX USB Interface.

It has been tested on RaspberryPi (Raspbian) with the Enttec DMXUSB Pro interface, but it should run ok on any unix environnement as long as liblo (>=0.26), python and standard ftdi sio module are available. It should also support any DMX USB Pro compatible hardware like DmxKing ultraDMX devices. Note that OpenDMX USB doesn't seems to work yet.


Install
-------------

Clone or Download this repo
```
  git clone https://github.com/Hemisphere-Project/HDmx.git
```


Dependencies
-------------

You can install the dependencies using the install.sh script (as root)
```
  cd HDmx
  sudo ./install.sh
```

Or manually
- **pySerial**: http://pyserial.sourceforge.net/pyserial.html#installation
- **liblo-dev and python-dev**: sudo apt-get install liblo-dev python-dev
- **pyLiblo**: http://das.nasophon.de/pyliblo/


Configuration
-------------

You can edit the HDmx script using a text editor to change the port number, the serial interfaces, ...
We will provide more settings a launch time later (using command line arguments).


Use
-------------

Plug your DMX-USB interface, and start HDmx !
```
  ./HDmx
```

You can now send OSC Command like this:
```
  /dmx/set <channel> <value>   : set channel (from 1 to 512) to value (from 0 to 255)
  /dmx/all						: set all channels to 255
  /dmx/off						: set all channels to 0
  /dmx/blackout   				: blackout every channels (using build in blackout)
  
```



Credits
-------------

HDmx is developped by Thomas BOHL (Maigre) from the Hemisphere-Project Team.

HDmx is build on top of:
```
	* pySerial from Chris Liechti
	* DmxPy from davepaul0 (embedded)
	* Liblo from Steve Harris and Stephen Sinclair 
	* pyLiblo from Dominic Sacré
```
and we thanks them for the hard work ;)

