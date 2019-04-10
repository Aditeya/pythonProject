#!/usr/bin/env python

import time

import opc

import threading

from interlaced_weave import moveRight

client = opc.Client('localhost:7890')

col = [(148, 0, 211),(75, 0, 103),(0, 0, 255),(0, 255, 0),(255, 255, 0),(255, 25, 0)]

ledColor = [(0,0,0)]*360
client.put_pixels(ledColor)
client.put_pixels(ledColor)

BG = list(ledColor)
time.sleep(1)

#ledColor[5] = (255,255,0)

offsetLIMIT = 54

def rain_Init():
	for x in range (0,2):
		ledColor[0*60+29+x] = col[0]
	client.put_pixels(ledColor)
	time.sleep(0.5)
	
	for x in range (0,2):
		ledColor[2*60+23+x] = col[1]
	client.put_pixels(ledColor)
	time.sleep(0.5)
	
	for x in range (0,2):
		ledColor[2*60+35+x] = col[2]
	client.put_pixels(ledColor)
	time.sleep(0.5)
	
	for x in range (0,2):
		ledColor[5*60+26+x] = col[3]
	client.put_pixels(ledColor)
	time.sleep(0.5)
	
	for x in range (0,2):
		ledColor[5*60+32+x] = col[4]
	client.put_pixels(ledColor)
	time.sleep(0.5)
	
	for x in range (0,2):
		for y in range (0,2):
			ledColor[(2+x)*60 + (29+y)] = col[5]
	client.put_pixels(ledColor)
	
#rain_Init()

def rainSwish(secs):
	i=0
	cNo = 0
	
	while cNo<6:
	
		for y in range (0,60):
			for x in range (0,6):
				ledColor[x*60 + y] = col[cNo]
				client.put_pixels(ledColor)
				time.sleep(0.005)
		cNo = cNo + 1
			

def rainRun():
	i=0
	cNo = -1
	x=0
	
	while i == 0:
			
		for y in range (0,60):
			if(y%10 == 0):
					cNo = cNo+1
			for x in range (0,6):
				if(cNo == 6):
					cNo = 0
				ledColor[x*60 + y] = col[cNo]
				time.sleep(0.001)
				client.put_pixels(ledColor)
				
		while True:
			moveRight(ledColor)
			client.put_pixels(ledColor)
			time.sleep(0.01)
					
			
		
		i = 1
			
def runColChng(cNo):
	for y in range(0, 6):
		ledColor[y*60] = col[cNo]
		client.put_pixels(ledColor)
			
def colRun(cNo):
	for y in range (0,60):
		for x in range (0,6):
			ledColor[x*60 + y] = col[cNo]
			client.put_pixels(ledColor)
			time.sleep(0.005)

#rainRun()



rainRun()

#for x in range (0, 60):
#	ledColor[0*60 + x+1] = ledColor[0*60 + x]
#	client.put_pixels(ledColor)
#	time.sleep(0.01)

			
				
