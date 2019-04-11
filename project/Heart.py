#!/usr/bin/env python

import time

import opc

client = opc.Client('localhost:7890')

ledColor = [(0,0,0)]*360

BG = list(ledColor)


#ledColor[5] = (255,255,0)

offsetLIMIT = 54

ledEnum = enumerate(ledColor)

def heartFrame1(offset):                    #Create and output the pixels for heart frame 1
	offset=offset+3

	if offset > offsetLIMIT:
		offset = offsetLIMIT
		
	for x in range(offset-3, offset+6):                  #
		for y in range(0, 6):                            # Reseting the Background to original stored in default
			ledColor[y*60+x] = BG[y*60+x]                #

	ledColor[2*60+offset] = (255,0,0)                 #  
	ledColor[2*60+2+offset] = (255,0,0)               #
	ledColor[3*60+offset] = (255,0,0)                 # Setting the pixels
	ledColor[3*60+1+offset] = (255,0,0)               # 
	ledColor[3*60+2+offset] = (255,0,0)               #
	ledColor[4*60+1+offset] = (255,0,0)               #
	
	client.put_pixels(ledColor)	
	
	return	
	
def heartFrame2(offset):                    #Create and output the pixels for heart frame 2
	offset=offset+3

	if offset > offsetLIMIT:
		offset = offsetLIMIT
		
	for x in range(offset-3, offset+6):                   #
		for y in range(0, 6):                             # Reseting the Background to original stored in default
			ledColor[y*60+x] = BG[y*60+x]	              #
		

	ledColor[1*60+offset] = (255,0,0)                 #  
	ledColor[1*60+2+offset] = (255,0,0)               #
	for x in range(-1, 4):                            # Setting the pixels
		ledColor[2*60+offset+x] = (255,0,0)           # 
	for x in range(0, 3):                             #
		ledColor[3*60+offset+x] = (255,0,0)           #
	ledColor[4*60+1+offset] = (255,0,0)
	
	client.put_pixels(ledColor)	
	
	
	return

def heartFrame3(offset):                    #Create and output the pixels for heart frame 3
	offset=offset+3

	if offset > offsetLIMIT:
		offset = offsetLIMIT
		
	for x in range(offset-3, offset+6):                   #
		for y in range(0, 6):                             # Reseting the Background to original stored in default
			ledColor[y*60+x] = BG[y*60+x]	              #	
		

	ledColor[0*60+offset-1] = (255,0,0)
	ledColor[0*60+offset+3] = (255,0,0)
	for x in range(-2, 5):
		if x != 1:
			ledColor[1*60+offset+x] = (255,0,0)       #  
	for x in range(-2, 5):                            #
		ledColor[2*60+offset+x] = (255,0,0)           # Setting the pixels
	for x in range(-1, 4):                            # 
		ledColor[3*60+offset+x] = (255,0,0)           #
	for x in range(0, 3):                             #
		ledColor[4*60+offset+x] = (255,0,0)    
	ledColor[5*60+offset+1] = (255,0,0)        
	
	client.put_pixels(ledColor)	
	
	return

def heartFrame4(offset):                    #Create and output the pixels for heart frame 4
	offset=offset+3
	
	if offset > offsetLIMIT:
		offset = offsetLIMIT
		
	for x in range(offset-3, offset+6):                   #
		for y in range(0, 6):                             # Reseting the Background to original stored in default
			ledColor[y*60+x] = BG[y*60+x]	              #	
			

	ledColor[0*60+offset-1] = (255,0,0)
	ledColor[0*60+offset-2] = (255,0,0)
	ledColor[0*60+offset+3] = (255,0,0)
	ledColor[0*60+offset+4] = (255,0,0)
	for x in range(-3, 6):
		ledColor[1*60+offset+x] = (255,0,0)           #  
	for x in range(-3, 6):                            #
		ledColor[2*60+offset+x] = (255,0,0)           # Setting the pixels
	for x in range(-2, 5):                            # 
		ledColor[3*60+offset+x] = (255,0,0)           #
	for x in range(-1, 4):                            #
		ledColor[4*60+offset+x] = (255,0,0)
	for x in range(0, 3):	
		ledColor[5*60+offset+1] = (255,0,0)
		
		
	client.put_pixels(ledColor)	
		
	return

client.put_pixels(ledColor)

def heartAnimation(speed, offsetA):    #Play the heart Animtion

	heartFrame1(offsetA)                    #output the pixels

	time.sleep((5/30.0)/speed)              #wait for the frames

	heartFrame2(offsetA)                    #Rinse repeat
	
	time.sleep((1/30.0)/speed)
	
	heartFrame3(offsetA)
	
	time.sleep((2/30.0)/speed)
	
	heartFrame4(offsetA)
	
	time.sleep((1/30.0)/speed)
	
	heartFrame3(offsetA)
	
	time.sleep((3/30.0)/speed)
	
	heartFrame2(offsetA)
	
	time.sleep((3/30)/speed)
	
	heartFrame3(offsetA)
	
	time.sleep((1/30.0)/speed)
	 
	heartFrame4(offsetA)
	
	time.sleep((2/30.0)/speed)
	  
	heartFrame3(offsetA)
	
	time.sleep((3/30.0)/speed)
					  
	heartFrame2(offsetA)
	
	time.sleep((3/30.0)/speed)
	
	heartFrame1(offsetA)
	
	time.sleep((1/30.0)/speed)

def heartAnimPlay():

	heartAnimation(1.5, 0)
	heartAnimation(1, 607)
	heartAnimation(0.75, 25)

	return ledColor

#heartFrame1(30,0)
#heartFrame4(30,0)
#heartFrame1(30,0)
#
#time.sleep(1)
#client.put_pixels(BG)


#for item in ledEnum:
#	print item

#client.put_pixels(ledColor)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
#client.put_pixels(led_colour)
