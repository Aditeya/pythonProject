#!/usr/bin/env python

import time

import opc

import threading

from random import randint

from interlaced_weave import moveRight
import winsound
# Play Windows exit sound.
#winsound.PlaySound("Rainbow.wav", winsound.SND_ASYNC)

client = opc.Client('localhost:7890')

col = [(255, 137, 198),(255, 172, 48),(255, 255, 81),(231, 235, 236),(160, 218, 242),(194, 106, 221)]

blackBG = [(0,0,0)]*360

ledColor = [(0,0,0)]*360
client.put_pixels(ledColor)
client.put_pixels(ledColor)

BG = list(ledColor)
time.sleep(1)

#ledColor[5] = (255,255,0)

offsetLIMIT = 54

def rain_Init():			# animation title 
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
	time.sleep(1)
	
	for x in range (0,2):
		for y in range (0,2):
			ledColor[(2+x)*60 + (29+y)] = col[5]
	client.put_pixels(ledColor)
	

def rain_Init_Ex(cs):				# animation title (instantaneos ver)

	if cs == 1:
		for y in range (0,6):
			for x in range (0, 60):
				ledColor[y*60 + x] = (0, 0, 0)

	for x in range (0,2):
		ledColor[0*60+29+x] = col[0]
	
	for x in range (0,2):
		ledColor[2*60+23+x] = col[1]
	
	for x in range (0,2):
		ledColor[2*60+35+x] = col[2]

	
	for x in range (0,2):
		ledColor[5*60+26+x] = col[3]
	
	for x in range (0,2):
		ledColor[5*60+32+x] = col[4]
	
	for x in range (0,2):
		for y in range (0,2):
			ledColor[(2+x)*60 + (29+y)] = col[5]
	
	client.put_pixels(ledColor)
	
	
def rain_Init_S():			# animation title (slow ver)


	for x in range(0, 60):
		ledColor[0*60+x] = (0, 0, 0)
		
	for x in range (0,2):
		ledColor[0*60+29+x] = col[0]
	time.sleep(0.75)
	client.put_pixels(ledColor)
	
	for x in range(0, 60):
		ledColor[1*60+x] = (0, 0, 0)
	time.sleep(0.75)
	client.put_pixels(ledColor)
	
	for x in range(0, 60):
		ledColor[2*60+x] = (0, 0, 0)
	
	for x in range (0,2):
		ledColor[2*60+23+x] = col[1]
		
	for x in range (0,2):
		ledColor[2*60+35+x] = col[2]
	time.sleep(0.75)
	client.put_pixels(ledColor)
	
	for x in range(0, 60):
		ledColor[3*60+x] = (0, 0, 0)
	time.sleep(0.75)
	client.put_pixels(ledColor)
	
	for x in range(0, 60):
		ledColor[4*60+x] = (0, 0, 0)
	time.sleep(0.75)
	client.put_pixels(ledColor)
	
	for x in range(0, 60):
		ledColor[5*60+x] = (0, 0, 0)
	
	for x in range (0,2):
		ledColor[5*60+26+x] = col[3]
		
	for x in range (0,2):
		ledColor[5*60+32+x] = col[4]
	time.sleep(0.75)
	client.put_pixels(ledColor)
	
	for x in range (0,2):
		for y in range (0,2):
			ledColor[(2+x)*60 + (29+y)] = col[5]
	time.sleep(3)
	client.put_pixels(ledColor)
	
#rain_Init()

def rainSwish():			#rainbow swishing animtion 
	i=0
	cNo = 0
	
	while cNo<6:
	
		for y in range (0,60):
			for x in range (0,6):
				ledColor[x*60 + y] = col[cNo]
			client.put_pixels(ledColor)
			time.sleep(0.005)
		cNo = cNo + 1
		
	return
		
def rainSwish_L():			#rainbow swishing animtion (Long ver)
	i=0
	cNo = 0
	
	while cNo<5:
	
		for y in range (0,60):
			for x in range (0,6):
				ledColor[x*60 + y] = col[cNo]
			client.put_pixels(ledColor)
			time.sleep(0.005)
		cNo = cNo + 1
		
	for y in range (0,30):
		for x in range (0,6):
			ledColor[x*60 + y] = col[cNo]
			client.put_pixels(ledColor)
			time.sleep(0.005)
			
	for y in range (30,60):
		for x in range (0,6):
			ledColor[x*60 + y] = col[cNo]
			client.put_pixels(ledColor)
			time.sleep(0.01)
	
	return	

def rainRunInit():			#intializer for rainRun
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
			time.sleep(0.02)
			client.put_pixels(ledColor)				
		
		i = 1
	
	return
	
def rainRun(iter):				# rainbow running animation
	
	while iter >=0:
		moveRight(ledColor)
		client.put_pixels(ledColor)
		time.sleep(0.01)
		iter-=1
		
	return
		
def rainBars(iter):				# Synthesizer animation
	
	while iter >=0:
		
		i=randint(0,5)
		threading.Thread(target=barAnim, args=(0, 5, i,)).start()
		time.sleep(0.05)
		
		i=randint(0,5)
		threading.Thread(target=barAnim, args=(10, 1, i,)).start()	
		time.sleep(0.05)
		
		i=randint(0,5)
		threading.Thread(target=barAnim, args=(20, 2, i,)).start()	
		time.sleep(0.05)
		
		i=randint(0,5)
		threading.Thread(target=barAnim, args=(30, 3, i,)).start()	
		time.sleep(0.05)
		
		i=randint(0,5)
		threading.Thread(target=barAnim, args=(40, 4, i,)).start()	
		time.sleep(0.05)
		
		i=randint(0,5)
		threading.Thread(target=barAnim, args=(50, 0, i,)).start()
		time.sleep(0.05)		
		
		iter-=1

	return
	
def barAnim(offset, cNo, i):
		
	b = i
	y = 5
	while i >= 0:
		
		for j in range(10):
			ledColor[y*60 + j + offset] = col[cNo]

		client.put_pixels(ledColor)
		time.sleep(0.025)
		y-=1
		i-=1
	
	
	while i <= b:
		
		
		for j in range(10):
			ledColor[y*60 + j + offset] = (0,0,0)
			
		client.put_pixels(ledColor)
		time.sleep(0.025)
		i+=1
		y+=1

	return


#rainRun()

def rainbowAnim():     #plays the Rainbow Animation
	
	winsound.PlaySound("Rainbow.wav", winsound.SND_ASYNC)
	time.sleep(3)
	rain_Init()
	time.sleep(2)
	client.put_pixels(blackBG)
	time.sleep(0.1)
	client.put_pixels(ledColor)
	time.sleep(1.8)
	client.put_pixels(blackBG)
	time.sleep(0.1)
	rainBars(22)
	rain_Init_Ex(0)
	time.sleep(0.1)
	client.put_pixels(blackBG)
	time.sleep(0.1)
	rain_Init_Ex(0)
	time.sleep(0.1)
	client.put_pixels(blackBG)
	time.sleep(0.1)
	rainSwish()
	rainSwish_L()
	time.sleep(0.1)
	client.put_pixels(blackBG)
	time.sleep(0.1)
	rain_Init_Ex(1)
	time.sleep(0.1)
	client.put_pixels(blackBG)
	time.sleep(0.1)
	rainBars(40)
	rainSwish_L()
	time.sleep(0.1)
	client.put_pixels(blackBG)
	rainRunInit()
	rainRun(2100)
	rain_Init_S()
	
	
	time.sleep(5)
	return ledColor


#rainbowAnim()

#rainBars(100)


#rain_Init()
#rainSwish()
#rainRunInit()
#rainRun(100)

#for x in range (0, 60):
#	ledColor[0*60 + x+1] = ledColor[0*60 + x]
#	client.put_pixels(ledColor)
#	time.sleep(0.01)

			
				
