#!/bin/bash

#INSTALL TEMP Dir
mkdir dependencies
cd dependencies

#PYTHON DMX using pySerial
wget https://pypi.python.org/packages/source/p/pyserial/pyserial-2.7.tar.gz#md5=794506184df83ef2290de0d18803dd11
tar -zxvf pyserial-2.7.tar.gz
cd pyserial-2.7/
sudo python setup.py install
cd ..

#OSC CTRL using Liblo and pyLiblo
sudo apt-get install python-dev liblo-dev -y
wget http://das.nasophon.de/download/pyliblo-0.9.2.tar.gz
tar -zxvf pyliblo-0.9.2.tar.gz
cd pyliblo-0.9.2
./setup.py build
sudo ./setup.py install
cd ..
cd ..
rm -R dependencies

