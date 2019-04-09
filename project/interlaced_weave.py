import time
import opc
import ledutils

def pattern1(frame):
	colour1 = (255,178,0)
	colour2 = (0,0,0)
	
	for y in range(6):
		for x in range(4):
			ledutils.addPixels(frame, 1, colour1) # red
			ledutils.addPixels(frame, 11, colour2)  # black
		
		ledutils.addPixels(frame, 1, colour1)  # red
		ledutils.addPixels(frame, 11-y, colour2) # black
		ledutils.addPixels(frame, y+1, colour2)  # black
		
def pattern2(frame):
	colour1 = (225,0,255)
	colour2 = (0,0,0)
	
	for y in range(6):
		ledutils.addPixels(frame, 11-y, colour2) # black
		
		for x in range(4):
			ledutils.addPixels(frame, 1, colour1) # red
			ledutils.addPixels(frame, 11, colour2)  # black
		
		ledutils.addPixels(frame, 1, colour1) # red
		ledutils.addPixels(frame, y, colour2)	  # black

def moveRight(strip):
	strip.insert(0, strip.pop(59))
	strip.insert(60, strip.pop(119))
	strip.insert(120, strip.pop(179))
	strip.insert(180, strip.pop(239))
	strip.insert(240, strip.pop(299))
	strip.insert(300, strip.pop(359))

def moveLeft(strip):
	strip.insert(59, strip.pop(0))
	strip.insert(119, strip.pop(60 ))
	strip.insert(179, strip.pop(120))
	strip.insert(239, strip.pop(180))
	strip.insert(299, strip.pop(240))
	strip.insert(359, strip.pop(300))

# Each frame is 0.1s
def interlacedWeave(frames):
	ADDRESS = 'localhost:7890'
	client = opc.Client(ADDRESS)
	
	frame1 = []
	frame2 = []
	
	pattern1(frame1)
	pattern2(frame2)
	
	i = 0
	while i < frames:
		client.put_pixels(frame1, channel=225)
		client.put_pixels(frame1, channel=225)
		moveLeft(frame1)
		time.sleep(0.05)
		client.put_pixels(frame2, channel=225)
		client.put_pixels(frame2, channel=225)
		moveRight(frame2)
		time.sleep(0.05)
		i+=1