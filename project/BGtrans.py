#!/usr/bin/env python

import time

import opc

import threading

client = opc.Client('localhost:7890')

ledColor = [(0,0,0)]*360

BG = list(ledColor)


#ledColor[5] = (255,255,0)

def verLineAnim(Up, loc, r, g, b)
	
	if Up = 0:
		for x in range(0, 5) 
			ledColor[x*60+loc] = (r, g, b)
			ledColor[x*60+loc+1] = (r, g, b)
			ledColor[x*60+loc+2] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.1)
			
	if Up = 1:
		for x in range(0, 5) 
			ledColor[(5-x)*60+loc] = (r, g, b)
			ledColor[(5-x)*60+loc+1] = (r, g, b)
			ledColor[(5-x)*60+loc+2] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.1)	

def horLineAnim(R, loc, r, g, b)
	
	if R = 0:
		for x in range(0, 59) 
			ledColor[loc*60+x] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.01)
	
	if R = 0:
		for x in range(0, 59) 
			ledColor[loc*60+(59-x)] = (r, g, b)
			client.put_pixels(ledColor)
			time.sleep(0.01)
			
threading.Thread(target=verLineAnim, args=(0, 0, 255, 255, 255,)).start()		

threading.Thread(target=verLineAnim, args=(0, 6, 255, 255, 255,)).start()		