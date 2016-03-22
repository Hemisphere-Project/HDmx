import serial
import sys

###CODE IMPORTED FROM ##############
#https://github.com/davepaul0/DmxPy#

DMXOPEN = chr(126)
DMXCLOSE = chr(231)
DMXINTENSITY=chr(6)+chr(1)+chr(2)
DMXINIT1= chr(03)+chr(02)+chr(0)+chr(0)+chr(0)
DMXINIT2= chr(10)+chr(02)+chr(0)+chr(0)+chr(0)

class DmxPy:
	def __init__(self, serialPort):
		try:
			self.serial=serial.Serial(serialPort, baudrate=57600)
		except:
			print "Error: could not open Serial Port "+serialPort
			sys.exit(0)
		self.serial.write( DMXOPEN+DMXINIT1+DMXCLOSE)
		self.serial.write( DMXOPEN+DMXINIT2+DMXCLOSE)
		self.dmxData=[chr(0)]*513   #128 plus "spacer".

	def set(self, chan, intensity):
		if chan > 512 : chan = 512
		if chan < 1 : return
		if intensity > 255 : intensity = 255
		if intensity < 0 : intensity = 0
		self.dmxData[chan] = chr(intensity)

	def setall(self, val=255):
		for i in xrange (1, 512, 1):
			self.dmxData[i] = chr(val)

	def render(self):
		sdata=''.join(self.dmxData)
		self.serial.write(DMXOPEN+DMXINTENSITY+sdata+DMXCLOSE)
######## END OF IMPORTED CODE #################
