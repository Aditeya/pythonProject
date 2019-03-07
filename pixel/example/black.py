#!/usr/bin/env python

import time

import opc

client = opc.Client('localhost:7890')

ledColor = [(225,225,225)]*360

ledColor[5] = (255,255,0)

ledEnum = enumerate(ledColor)

def heartFrame1(frames, offset):
	offset=offset+3
	ledColor[2*60+offset] = (255,0,0)
	ledColor[2*60+2+offset] = (255,0,0)
	ledColor[3*60+offset] = (255,0,0)
	ledColor[3*60+1+offset] = (255,0,0)
	ledColor[3*60+2+offset] = (255,0,0)
	ledColor[4*60+1+offset] = (255,0,0)
	
	return	
	
def heartFrame2(frames, offset):
	offset=offset+3
	ledColor[1*60+offset] = (255,0,0)
	ledColor[1*60+2+offset] = (255,0,0)
	for x in range(-1, 4):
		ledColor[2*60+offset+x] = (255,0,0)
	for x in range(1, 3):
		ledColor[3*60+offset+x] = (255,0,0)
	ledColor[4*60+1+offset] = (255,0,0)	

def heartFrame3(frames, offset):
	offset=offset+3
	ledColor[0*60+offset-1] = (255,0,0)
	ledColor[0*60+offset+3] = (255,0,0)
	for x in range(-2, 5):
		if x != 1:
			ledColor[1*60+offset+x] = (255,0,0)
	for x in range(-2, 5):
		ledColor[2*60+offset+x] = (255,0,0)
	for x in range(-1, 4):
		ledColor[3*60+offset+x] = (255,0,0)
	for x in range(0, 3):
		ledColor[4*60+offset+x] = (255,0,0)
	ledColor[5*60+offset+1] = (255,0,0)

def heartFrame4(frames, offset):
	offset=offset+3
	ledColor[0*60+offset-1] = (255,0,0)
	ledColor[0*60+offset-2] = (255,0,0)
	ledColor[0*60+offset+3] = (255,0,0)
	ledColor[0*60+offset+4] = (255,0,0)
	for x in range(-3, 6):
		ledColor[1*60+offset+x] = (255,0,0)
	for x in range(-3, 6):
		ledColor[2*60+offset+x] = (255,0,0)
	for x in range(-2, 5):
		ledColor[3*60+offset+x] = (255,0,0)
	for x in range(-1, 4):
		ledColor[4*60+offset+x] = (255,0,0)
	for x in range(0, 3):	
		ledColor[5*60+offset+1] = (255,0,0)	
		
heartFrame1(1,0)
heartFrame1(1,10)
client.put_pixels(ledColor)
time.sleep(1)
heartFrame2(1,0)
heartFrame2(1,10)
client.put_pixels(ledColor)
time.sleep(1)
heartFrame3(1,0)
heartFrame3(1,10)
client.put_pixels(ledColor)
time.sleep(1)
heartFrame4(1,0)
heartFrame4(1,10)
client.put_pixels(ledColor)

#for item in ledEnum:
#	print item

client.put_pixels(ledColor)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
#client.put_pixels(led_colour)
