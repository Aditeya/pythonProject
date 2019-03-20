#import sys
import opc
import time

"""
ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)

if client.can_connect():
    print('connected to %s' % ADDRESS)
else:
	print('WARNING: could not connect to %s' % ADDRESS)
	sys.exit()
"""

#
def blackPixels(strip, n):
	strip += [(0,0,0)]*n
	return

#
def redPixels(strip, n):
	strip += [(255,0,0)]*n
	return
	
#
def createStrip1(strip1):

	blackPixels(strip1,2)
	
	i=0
	while i < 4:
		redPixels(strip1,2)
		blackPixels(strip1,10)
		i+=1
	
	redPixels(strip1,2)
	blackPixels(strip1,8)

#
def createStrip2(strip2):

	blackPixels(strip2,1)
	
	i=0
	while i < 4:
		redPixels(strip2,1)
		blackPixels(strip2,2)
		redPixels(strip2,1)
		blackPixels(strip2,8)
		i+=1
	
	redPixels(strip2,1)
	blackPixels(strip2,2)
	redPixels(strip2,1)
	blackPixels(strip2,7)

#
def createStrip3(strip3):

	i=0
	while i < 5:
		redPixels(strip3,1)
		blackPixels(strip3,4)
		redPixels(strip3,1)
		blackPixels(strip3,6)
		i+=1

#
def createStrip4(strip4):

	strip = []
	createStrip3(strip)
	i=0
	while i < 6:
		strip.insert(0, strip.pop(59))
		i+=1
	strip4 += strip

#
def createStrip5(strip5):

	strip = []
	createStrip2(strip)
	i=0
	while i < 6:
		strip.insert(0, strip.pop(59))
		i+=1
	strip5 += strip

#
def createStrip6(strip6):

	strip = []
	createStrip1(strip)
	i=0
	while i < 6:
		strip.insert(0, strip.pop(59))
		i+=1
	strip6 += strip

#
def createStrip(strip):
	createStrip1(strip)
	createStrip2(strip)
	createStrip3(strip)
	createStrip4(strip)
	createStrip5(strip)
	createStrip6(strip)

#
def moveStrip(strip):
	strip.insert(0, strip.pop(59))
	strip.insert(60, strip.pop(119))
	strip.insert(120, strip.pop(179))
	strip.insert(180, strip.pop(239))
	strip.insert(240, strip.pop(299))
	strip.insert(300, strip.pop(359))

#
def run(strip, j):
	client = opc.Client('localhost:7890')
	i=0
	while i < j:
		#client.put_pixels(strip,channel=255)
		moveStrip(strip)
		client.put_pixels(strip,channel=255)
		time.sleep(0.025)
		i+=1

#
def createAndPlayStrip(frames):
	client = opc.Client('localhost:7890')
	strip = []
	createStrip(strip)
	#strip[3*60+0] = (255,255,255)  i = 60r + l
	client.put_pixels(strip,channel=255)
	run(strip, frames)
	
#createAndPlayStrip(400)


