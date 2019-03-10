import sys
import opc
import time

ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)

if client.can_connect():
    print('connected to %s' % ADDRESS)
else:
	print('WARNING: could not connect to %s' % ADDRESS)
	sys.exit()

def createStrip1(strip):
	i=0
	while i < 60:
		strip += [(0,0,0)]
		strip += [(255,0,0)]
		i+=2
		
def createStrip2(strip):
	i=0
	while i < 60:
		strip += [(255,0,0)]
		strip += [(0,0,0)]
		i+=2
		
def createStrip(strip):
	i=0
	while i < 6:
		createStrip1(strip)
		createStrip2(strip)
		i+=1
		
#

def moveStrip(strip):
	strip.insert(0, strip.pop(59))
	strip.insert(60, strip.pop(119))
	strip.insert(120, strip.pop(179))
	strip.insert(180, strip.pop(239))
	strip.insert(240, strip.pop(299))
	strip.insert(300, strip.pop(359))
	
def run(strip, j):

	i=0
	while i < j:
		#client.put_pixels(strip,channel=255)
		moveStrip(strip)
		client.put_pixels(strip,channel=255)
		time.sleep(1/5.0)
		i+=1

#		
def createAndPlayStrip(frames):

	strip = []
	createStrip(strip)
	#strip[3*60+0] = (255,255,255)  i = 60r + l
	client.put_pixels(strip,channel=255)
	run(strip, frames)
	
createAndPlayStrip(40)