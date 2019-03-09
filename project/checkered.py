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

def createStrip(strip):
	i=0
	while i < 360:
		strip += [(0,0,0)]
		strip += [(255,0,0)]
		i+=2
		
#

def moveStrip(strip):
	strip.insert(0, strip.pop(59))
	strip.insert(60, strip.pop(119))
	strip.insert(120, strip.pop(179))
	strip.insert(180, strip.pop(239))
	strip.insert(240, strip.pop(299))
	strip.insert(300, strip.pop(359))
	
