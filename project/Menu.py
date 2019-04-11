#!/usr/bin/env python

import time

import opc

import threading

import msvcrt

import menuDisp

import Heart

import pipes

import BGtransition

import SineWave

import checkered

import interlaced_weave

import Rainbow

client = opc.Client('localhost:7890')

print("press 'escape' to quit...")
text=""
i=0

sel = 0	

blackBG = [(0, 0, 0)]*360
	
open = True

menuDisp.menuTitle()

while open:
	#showMenu()
	char = msvcrt.getwch()
	if(ord(char) == 80):				#Checks for key input and changes the cyclic selection acc
		if(sel == 6):
			sel = 0
		else:
			sel = sel+1
		menuDisp.menuSel(sel)
		print(sel)
	
	elif(ord(char) == 72):
		if(sel == 0):
			sel = 6
		else:
			sel = sel-1
		menuDisp.menuSel(sel)
		print(sel)
	
	elif(ord(char) == 13):					#checks for enter input
		print("you chose ", sel)
		open = menuDisp.menuSel(sel)
		
		if(sel == 0):         #exit the program
			open = False
			client.put_pixels(blackBG)
			print("exiting")
			break
		
		elif(sel == 1):            #play sine wave
			client.put_pixels(blackBG)
			time.sleep(0.1)
			menuDisp.menuSel(sel)
			for x in range(0,3):
				time.sleep(0.05)
				client.put_pixels(blackBG)
				time.sleep(0.05)
				menuDisp.menuSel(sel)
			
			time.sleep(0.01)
			client.put_pixels(blackBG)
			time.sleep(1)
			ledColor = SineWave.createAndPlayStrip(100)
			time.sleep(1)
			BGtransition.BGTransAnim(255, 69, 12, 0, 0, 0, ledColor)
			time.sleep(3)
			menuDisp.menuTitle()
			
		elif(sel == 2):            #play checks
			client.put_pixels(blackBG)
			time.sleep(0.1)
			menuDisp.menuSel(sel)
			for x in range(0,3):
				time.sleep(0.05)
				client.put_pixels(blackBG)
				time.sleep(0.05)
				menuDisp.menuSel(sel)
			
			time.sleep(0.01)
			client.put_pixels(blackBG)
			time.sleep(1)
			ledColor = checkered.createAndPlayStrip(50)
			time.sleep(1)
			BGtransition.BGTransAnim(5, 168, 7, 0, 0, 0, ledColor)
			time.sleep(3)
			menuDisp.menuTitle()
			
		elif(sel == 3):					#Play Weave
			client.put_pixels(blackBG)
			time.sleep(0.1)
			menuDisp.menuSel(sel)
			for x in range(0,3):
				time.sleep(0.05)
				client.put_pixels(blackBG)
				time.sleep(0.05)
				menuDisp.menuSel(sel)
			
			time.sleep(0.01)
			client.put_pixels(blackBG)
			time.sleep(1)
			ledColor = interlaced_weave.interlacedWeave(50)
			time.sleep(1)
			BGtransition.BGTransAnim(5, 120, 196, 0, 0, 0, ledColor)
			time.sleep(3)
			menuDisp.menuTitle()
		
		elif(sel == 4):					#Play Heart
			client.put_pixels(blackBG)
			time.sleep(0.1)
			menuDisp.menuSel(sel)
			for x in range(0,3):
				time.sleep(0.05)
				client.put_pixels(blackBG)
				time.sleep(0.05)
				menuDisp.menuSel(sel)
			
			time.sleep(0.01)
			client.put_pixels(blackBG)
			time.sleep(1)
			ledColor = Heart.heartAnimPlay()
			time.sleep(1)
			BGtransition.BGTransAnim(255, 100, 100, 0, 0, 0, ledColor)
			time.sleep(3)
			menuDisp.menuTitle()
		
		elif(sel == 5):				#Play Pipes
			client.put_pixels(blackBG)
			time.sleep(0.1)
			menuDisp.menuSel(sel)
			for x in range(0,3):
				time.sleep(0.05)
				client.put_pixels(blackBG)
				time.sleep(0.05)
				menuDisp.menuSel(sel)
			
			time.sleep(0.01)
			client.put_pixels(blackBG)
			time.sleep(1)
			ledColor = pipes.playPipes(1)
			time.sleep(1)
			BGtransition.BGTransAnim(244, 192, 38, 0, 0, 0, ledColor)
			time.sleep(3)
			menuDisp.menuTitle()
			
		elif(sel == 6):				#Play Rainbow
			client.put_pixels(blackBG)
			time.sleep(0.1)
			menuDisp.menuSel(sel)
			for x in range(0,3):
				time.sleep(0.05)
				client.put_pixels(blackBG)
				time.sleep(0.05)
				menuDisp.menuSel(sel)
			
			time.sleep(0.01)
			client.put_pixels(blackBG)
			time.sleep(1)
			ledColor = Rainbow.rainbowAnim()
			time.sleep(1)
			BGtransition.BGTransAnim(88, 7, 132, 0, 0, 0, ledColor)
			time.sleep(3)
			menuDisp.menuTitle()
			
			

client = opc.Client('localhost:7890')

ledColor = [(0, 0, 0)]*360

BG = list(ledColor)

#client.put_pixels(ledColor)


#ledColor[5] = (255,255,0)



		
#time.sleep(0.01)
#threading.Thread(target=verLineAnim, args=(0, 6, 255, 255, 255,)).start()	
#time.sleep(0.01)
#threading.Thread(target=horLineAnim, args=(0, 0, 0, 255, 255,)).start()	




