"""
Script to test a COM to see when it has logged in

Basic functionality is given but extra code needs to be added

You might find this helpful

pattern = r'match'
matchObj = re.match( pattern, string, flags=0)
if matchObj
	do something

"""

import serial
import sys
import re

# configure the serial connections
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=None
)

ser.isOpen()

input=1
while 1 :
    if input == 'exit':
        ser.close()
	print '\r\n>> YAY, WE\'RE DONE'
        exit()
    else:
	out = ''
	# read data and display
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
	    sys.stdout.write(out)
