#!/usr/bin/env python

import time

import opc

import threading

client = opc.Client('localhost:7890')

#ledColor = [(0,0,0)]*360

#BG = list(ledColor)

#client.put_pixels(ledColor)


#ledColor[5] = (255,255,0)

def verLineAnim(Up, loc, r, g, b, ledColor):		#Animation for vertical line
	
	if Up == 0:
		for x in range(0, 6):
			ledColor[x*60+loc] = (r, g, b)
			ledColor[x*60+loc+1] = (r, g, b)
			ledColor[x*60+loc+2] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.05)
			
	if Up == 1:
		for x in range(0, 6):
			ledColor[(5-x)*60+loc] = (r, g, b)
			ledColor[(5-x)*60+loc+1] = (r, g, b)
			ledColor[(5-x)*60+loc+2] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.05)	
			
	return

def horLineAnim(R, loc, r, g, b, ledColor):		#Animation for horizontal line
	
	if R == 0:
		for x in range(0, 60):
			ledColor[loc*60+x] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.025)
	
	if R == 1:
		for x in range(0, 60):
			ledColor[loc*60+(59-x)] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.025)
			
	return



def BGTransAnim(r1, g1, b1, r2, g2, b2, ledColor):		#Plays the animation

	for i in range(0, 60, 6):
		threading.Thread(target=verLineAnim, args=(0, i, r1, g1, b1, ledColor,)).start()
		threading.Thread(target=verLineAnim, args=(1, i+3, r1-25, g1-25, b1-25, ledColor,)).start()
		time.sleep(0.1)
		
	time.sleep(1.5)

	for i in range(0, 6, 2):
		threading.Thread(target=horLineAnim, args=(0, i, r2, g2, b2, ledColor,)).start()
		threading.Thread(target=horLineAnim, args=(1, i+1, r2, g2, b2, ledColor,)).start()
		time.sleep(0.1)

	return


		
#time.sleep(0.01)
#threading.Thread(target=verLineAnim, args=(0, 6, 255, 255, 255,)).start()	
#time.sleep(0.01)
#threading.Thread(target=horLineAnim, args=(0, 0, 0, 255, 255,)).start()	