import opc
import time

def whiteLine(pixels):
	i=0
	while i < 60:
		pixels.insert(0,(0,0,0))
		i += 1
	return

# Create a client object
client = opc.Client('localhost:7890')

# Test if it can connect (optional)
ADDRESS = 'localhost:7890'

if client.can_connect():
    print('connected to %s' % ADDRESS)
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print('WARNING: could not connect to %s' % ADDRESS)

# Send pixels forever at 30 frames per second
my_pixels = [(255, 255, 255)]
i=0
while i < 6:
	
	if client.put_pixels(my_pixels, channel=0):
		whiteLine(my_pixels)
		i += 1
	else:
		print('not connected')
	time.sleep(1/30.0)
	#i += 1
	
