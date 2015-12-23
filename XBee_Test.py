import sys, serial, argparse
from time import sleep
from collections import deque
from xbee import XBee,ZigBee
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

"""
	XBee communication and datalogging via Python application. 
		Processing? 

	See https://gist.github.com/electronut/d5e5f68c610821e311b0/ 
"""

# plot class
class AnalogPlot:
  	# constr
  	def __init__(self, strPort, maxLen):
  	    # open serial port
  	    self.ser = serial.Serial(strPort, 9600)
	
  	    self.ax = deque([0.0]*maxLen)
  	    self.ay = deque([0.0]*maxLen)
  	    self.maxLen = maxLen
	
  	# add to buffer
  	def addToBuf(self, buf, val):
  	    if len(buf) < self.maxLen:
  	        buf.append(val)
  	    else:
  	        buf.pop()
  	        buf.appendleft(val)
	
  	# add data
  	def add(self, data):
  	    assert(len(data) == 2)
  	    self.addToBuf(self.ax, data[0])
  	    self.addToBuf(self.ay, data[1])
	
  	# update plot
  	def update(self, frameNum, a0, a1):
  	    try:
  	        line = self.ser.readline()
  	        data = [float(val) for val in line.split()]
  	        # print data
  	        if(len(data) == 2):
  	            self.add(data)
  	            a0.set_data(range(self.maxLen), self.ax)
  	            a1.set_data(range(self.maxLen), self.ay)
  	    except KeyboardInterrupt:
  	        print('exiting')
  	    
  	    return a0, 
	
  	# clean up
  	def close(self):
  	    # close serial
  	    self.ser.flush()
  	    self.ser.close()    


# ser = serial.Serial('/dev/ttyUSB0', 9600) # TODO: get correct port name 

# Use an XBee 802.15.4 device
# To use with an XBee ZigBee device, replace with:
#xbee = ZigBee(ser)

# xbee = XBee(ser)

# # Set remote DIO pin 2 to low (mode 4)
# xbee.remote_at(
#     dest_addr='\x56\x78',
#     command='D2',
#     parameter='\x04')

# xbee.remote_at(
#     dest_addr='\x56\x78',
#     command='WR')


