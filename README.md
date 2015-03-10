# HDmx
Simple OSC controllable DMX interface - Python

What is it
-------------

This is a python program listening OSC on port 3000, 
and sending command to DMX USB Interfaces like Enttec DMXUSB Pro (tested).

It's based on Liblo / pyLiblo for the OSC communication 
and pySerial + DmxPy for the DMX communication.


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
  
