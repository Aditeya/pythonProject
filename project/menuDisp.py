#!/usr/bin/env python

import time

import opc

import threading

from ledutils import addPixels

client = opc.Client('localhost:7890')


ledColor = [(0, 0, 0)]*360

#Below are all title functions

def heartTitle():

	for y in range (0, 6):
		for x in range (0, 60):
			ledColor[y*60+x] = (0,0,0)
		
	for y in range (0, 6):
		for x in (10, 15, 18, 25, 30, 33, 38, 43):
			ledColor[y*60+x] = (255,0,0)
	
	for	x in (11, 12, 13, 14, 19, 20, 21, 26, 27, 28, 29, 34, 35, 36, 37):
		ledColor[2*60+x] = (255,0,0)
	
	for x in (19, 20 ,21 ,22 ,23, 26, 27, 28, 29, 34, 35, 36, 37, 40, 41, 42, 44, 45, 46):
		ledColor[0*60+x] = (255,0,0)
		
	for x in (19, 20 ,21 ,22 ,23):
		ledColor[5*60+x] = (255,0,0)
		
	ledColor[3*60+36] = (255,0,0)
	ledColor[3*60+38] = (0,0,0)
	
	ledColor[4*60+37] = (255,0,0)
	ledColor[4*60+38] = (0,0,0)
	
	client.put_pixels(ledColor)			
		
	return
	
def pipesTitle():

	strip = []
	black = (0,0,0)
	green = (0,255,127)
	
	# 8 4 6 5 5 4 6 5 6 3 8
	addPixels(strip, 8, black)
	addPixels(strip, 4,green)
	addPixels(strip, 6, black)
	addPixels(strip, 5 ,green)
	addPixels(strip, 5, black)
	addPixels(strip, 4 ,green)
	addPixels(strip, 6 ,black)
	addPixels(strip, 5,green)
	addPixels(strip, 6,black)
	addPixels(strip, 3,green)
	addPixels(strip, 8,black)
	
	# 8 131 717 131 5 1 9 131 7
	addPixels(strip, 8, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 3, black)
	addPixels(strip, 1, green)
	
	addPixels(strip, 7, black)
	addPixels(strip, 1, green)
	addPixels(strip, 7, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 3, black)
	addPixels(strip, 1, green)
	
	addPixels(strip, 5, black)
	addPixels(strip, 1, green)
	addPixels(strip, 9, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 3, black)
	addPixels(strip, 1, green)
	
	addPixels(strip, 7,black)
	
	# 8 131 717 131 538 29
	addPixels(strip, 8, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 3, black)
	addPixels(strip, 1, green)
	
	addPixels(strip, 7, black)
	addPixels(strip, 1, green)
	addPixels(strip, 7, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 3, black)
	addPixels(strip, 1, green)
	
	addPixels(strip, 5, black)
	addPixels(strip, 3, green)
	addPixels(strip, 8, black)
	
	addPixels(strip, 2, green)
	addPixels(strip, 9, black)
	
	# 848 174 63 (10) 18
	addPixels(strip, 8, black)
	addPixels(strip, 4, green)
	addPixels(strip, 8, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 7, black)
	addPixels(strip, 4, green)
	
	addPixels(strip, 6, black)
	addPixels(strip, 3, green)
	
	addPixels(strip, 10, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 8, black)
	
	# 81(11) 171 919 131 7
	addPixels(strip, 8, black)
	addPixels(strip, 1, green)
	addPixels(strip, 11, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 7, black)
	addPixels(strip, 1, green)
	
	addPixels(strip, 9, black)
	addPixels(strip, 1, green)
	addPixels(strip, 9, black)
	
	addPixels(strip, 1, green)
	addPixels(strip, 3, black)
	addPixels(strip, 1, green)
	addPixels(strip, 7, black)
	
	# 819 551 956 38
	addPixels(strip, 8, black)
	addPixels(strip, 1, green)
	addPixels(strip, 9, black)
	
	addPixels(strip, 5, green)
	addPixels(strip, 5, black)
	addPixels(strip, 1, green)
	
	addPixels(strip, 9, black)
	addPixels(strip, 5, green)
	addPixels(strip, 6, black)
	
	addPixels(strip, 3, green)
	addPixels(strip, 8, black)

	
	#
	client.put_pixels(strip)

	
	return

def menuTitle():

	for y in range (0, 6):
		for x in range (0, 60):
			ledColor[y*60+x] = (0,0,0)

	blue = (39, 83, 244)
	black = (0, 0, 0)
	
	for y in (2,3):
		for x in range(0, 13):
			ledColor[y*60+x] = blue
		for x in range(47, 60):
			ledColor[y*60+x] = blue
		for x in (9, 13, 46, 50):
			ledColor[y*60+x] = black
			
	for y in range(0, 6):
		for x in (16, 22, 25, 31, 36, 38, 42):
			ledColor[y*60+x] = blue
			
	for x in (17, 21, 26, 27, 28, 29):
		ledColor[0*60+x] = blue
		
	for x in (17, 21, 32):
		ledColor[1*60+x] = blue
		
	for x in (18, 20, 26, 27, 33):
		ledColor[2*60+x] = blue
		
	for x in (19, 34):
		ledColor[3*60+x] = blue
		
	for x in (35, 39, 41):
		ledColor[4*60+x] = blue
		
	for x in range(25, 30):
		ledColor[5*60+x] = blue	
	
	for x in range(39, 42):
		ledColor[5*60+x] = blue
			
	client.put_pixels(ledColor)		
	
	return
	
def sineTitle():
	strip = []
	black = (0,0,0)
	orange = (255,92,0)
	
	# (19) 3 312 141 43(19)
	addPixels(strip, 19, black)
	addPixels(strip, 3, orange)
	
	addPixels(strip, 3, black)
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 4, black)
	addPixels(strip, 1, orange)
	
	addPixels(strip, 4, black)
	addPixels(strip, 3, orange)
	addPixels(strip, 19, black)
	
	# (18)16 122 313 1(22)
	addPixels(strip, 18, black)
	addPixels(strip, 1, orange)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	addPixels(strip, 2, orange)
	
	addPixels(strip, 3, black)
	addPixels(strip, 1, orange)
	addPixels(strip, 3, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 22, black)
	
	# (18)16 123 212 2(22)
	addPixels(strip, 18, black)
	addPixels(strip, 1, orange)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	addPixels(strip, 3, orange)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	
	addPixels(strip, 2, orange)
	addPixels(strip, 22, black)
	
	# (19)33 121 121 141 (21)
	addPixels(strip, 19, black)
	addPixels(strip, 3, orange)
	addPixels(strip, 3, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	addPixels(strip, 1, orange)
	
	addPixels(strip, 1, black)
	addPixels(strip, 2, orange)
	addPixels(strip, 1, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 4, black)
	addPixels(strip, 1, orange)
	
	addPixels(strip, 21, black)
	
	# (22) 121212 331 (22)
	addPixels(strip, 22, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	
	addPixels(strip, 3, orange)
	addPixels(strip, 3, black)
	addPixels(strip, 1, orange)
	
	addPixels(strip, 22,black)
	
	# (18)43 121 322 5(19)
	addPixels(strip, 18, black)
	addPixels(strip, 4, orange)
	addPixels(strip, 3, black)
	
	addPixels(strip, 1, orange)
	addPixels(strip, 2, black)
	addPixels(strip, 1, orange)
	
	addPixels(strip, 3, black)
	addPixels(strip, 2, orange)
	addPixels(strip, 2, black)
	
	addPixels(strip, 5, orange)
	addPixels(strip, 19,black)
	
	client.put_pixels(strip)

def checksTitle():

	strip = []
	black = (0,0,0)
	yellow = (255,255,0)
	
	# (10)52 131 25252 1212 5(11)
	addPixels(strip, 10, black)
	addPixels(strip, 5, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 3, black)
	addPixels(strip, 1, yellow)
	
	addPixels(strip, 2, black)
	addPixels(strip, 5, yellow)
	addPixels(strip, 2, black)
	addPixels(strip, 5, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 2, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 5, yellow)
	addPixels(strip, 11, black)
	
	# (10)16 131 21616 111 31(15)
	addPixels(strip, 10, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 3, black)
	addPixels(strip, 1, yellow)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 1, black)
	addPixels(strip, 1, yellow)
	
	addPixels(strip, 3, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 15, black)
	
	# (10)16 523 416 241 (15)
	addPixels(strip, 10, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 5, yellow)
	addPixels(strip, 2, black)
	addPixels(strip, 3, yellow)
	
	addPixels(strip, 4, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 2, yellow)
	addPixels(strip, 4, black)
	addPixels(strip, 1, yellow)
	
	addPixels(strip, 15, black)
	
	# (10)16 1312 1616 111 35(11)
	addPixels(strip, 10, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 3, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 1, black)
	addPixels(strip, 1, yellow)
	
	addPixels(strip, 3, black)
	addPixels(strip, 5, yellow)
	addPixels(strip, 11, black)
	
	# (10)16 1312 1616 121 61(11)
	addPixels(strip, 10, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 3, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 2, black)
	addPixels(strip, 1, yellow)
	
	addPixels(strip, 6, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 11, black)
	
	# (10)52 1312 5252 131 15(11)
	addPixels(strip, 10, black)
	addPixels(strip, 5, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 3, black)
	addPixels(strip, 1, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 5, yellow)
	addPixels(strip, 2, black)
	addPixels(strip, 5, yellow)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, yellow)
	addPixels(strip, 3, black)
	addPixels(strip, 1, yellow)
	
	addPixels(strip, 1, black)
	addPixels(strip, 5, yellow)
	addPixels(strip, 11, black)
	
	client.put_pixels(strip)

def weaveTitle():

	strip = []
	black = (0,0,0)
	purple = (130,0,255)
	
	
	# (13) 151 344 13131 24 (14)
	addPixels(strip, 13, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 5, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 3, black)
	addPixels(strip, 4, purple)
	addPixels(strip, 4, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 3, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 3, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 4, purple)
	addPixels(strip, 14, black)
	
	# (13) 15121 7111 213 111 4 (14)
	addPixels(strip, 13, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 5, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 2, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 7, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 3, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 18, black)
	
	# (13) 151 235 111 213 113 (16)
	addPixels(strip, 13, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 5, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 3, purple)
	addPixels(strip, 5, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 3, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 3, purple)
	
	addPixels(strip, 16, black)
	
	# (14) 11111 316 11111 2111 21 (18)
	addPixels(strip, 14, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 3, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 18, black)
	
	# (14) 11111 316 131  2111 21 (18)
	addPixels(strip, 14, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 3, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 6, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 3, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 2, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 18, black)
	
	# (15) 111 542 131 314 4 (14)
	addPixels(strip, 15, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 1, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 5, black)
	addPixels(strip, 4, purple)
	addPixels(strip, 2, black)
	
	addPixels(strip, 1, purple)
	addPixels(strip, 3, black)
	addPixels(strip, 1, purple)
	
	addPixels(strip, 3, black)
	addPixels(strip, 1, purple)
	addPixels(strip, 4, black)
	
	addPixels(strip, 4, purple)
	addPixels(strip, 14, black)
	
	client.put_pixels(strip)

def extTitle():

	for y in range (0, 6):
		for x in range (0, 60):
			ledColor[y*60+x] = (0,0,0)
	
	for y in range(0, 6):
		for x in (20, 27, 30, 33, 38):
			ledColor[y*60+x] = (255,255,255)
			
	for x in range(20, 25):
		ledColor[0*60+x] = (255,255,255)
	
	for x in range(35, 42):
		ledColor[0*60+x] = (255,255,255)
		
	for x in (21, 22, 28, 29):
		ledColor[2*60+x] = (255,255,255)
	
	for x in (27, 30):
		ledColor[2*60+x] = (0, 0, 0)
		
	for x in (28, 29):
		ledColor[3*60+x] = (255,255,255)
	
	for x in (27, 30):
		ledColor[3*60+x] = (0, 0, 0)
	
	for x in (21, 22, 28, 29):
		ledColor[2*60+x] = (255,255,255)
		
	for x in range(20, 25):
		ledColor[5*60+x] = (255,255,255)
		
	client.put_pixels(ledColor)			
	
	return

def rainTitle():

	strip = []
	black = (0,0,0)
	purple = (194,106,221)
	blue = (160,218,242)
	white = (255,255,255)
	yellow = (255,255,81)
	orange = (255,172,48)
	pink = (255,137,198)
	
	# 1
	addPixels(strip, 7,black)
	addPixels(strip, 4,purple)
	addPixels(strip, 4,black)
	
	addPixels(strip, 3,blue)
	addPixels(strip, 2,black)
	
	addPixels(strip, 5,white)
	addPixels(strip, 2,black)
	
	addPixels(strip, 2,yellow)
	addPixels(strip, 2,black)
	addPixels(strip, 1,yellow)
	addPixels(strip, 2,black)
	
	addPixels(strip, 4,orange)
	addPixels(strip, 4,black)
	
	addPixels(strip, 3,pink)
	addPixels(strip, 3,black)
	
	addPixels(strip, 1,purple)
	addPixels(strip, 3,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 7,black)
	
	# 2
	addPixels(strip, 7,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 3,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 3,black)
	
	addPixels(strip, 1,blue)
	addPixels(strip, 1,black)
	addPixels(strip, 1,blue)
	
	addPixels(strip, 4,black)
	addPixels(strip, 1,white)
	addPixels(strip, 4,black)
	
	addPixels(strip, 2,yellow)
	addPixels(strip, 2,black)
	addPixels(strip, 1,yellow)
	
	addPixels(strip, 2,black)
	addPixels(strip, 1,orange)
	addPixels(strip, 3,black)
	addPixels(strip, 1,orange)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,pink)
	addPixels(strip, 3,black)
	addPixels(strip, 1,pink)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,purple)
	addPixels(strip, 3,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 7,black)
	
	# 3
	addPixels(strip, 7,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 2,black)
	addPixels(strip, 2,purple)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,blue)
	addPixels(strip, 3,black)
	addPixels(strip, 1,blue)
	
	addPixels(strip, 3,black)
	addPixels(strip, 1,white)
	addPixels(strip, 4,black)
	
	addPixels(strip, 1,yellow)
	addPixels(strip, 1,black)
	addPixels(strip, 1,yellow)
	addPixels(strip, 1,black)
	addPixels(strip, 1,yellow)
	
	addPixels(strip, 2,black)
	addPixels(strip, 1,orange)
	addPixels(strip, 1,black)
	addPixels(strip, 2,orange)
	addPixels(strip, 3,black)
	
	addPixels(strip, 1,pink)
	addPixels(strip, 3,black)
	addPixels(strip, 1,pink)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,purple)
	addPixels(strip, 3,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 7,black)
	
	# 4
	addPixels(strip, 7,black)
	addPixels(strip, 3,purple)
	addPixels(strip, 4,black)
	
	addPixels(strip, 5,blue)
	
	addPixels(strip, 3,black)
	addPixels(strip, 1,white)
	addPixels(strip, 4,black)
	
	addPixels(strip, 1,yellow)
	addPixels(strip, 1,black)
	addPixels(strip, 3,yellow)
	
	addPixels(strip, 2,black)
	addPixels(strip, 1,orange)
	addPixels(strip, 3,black)
	addPixels(strip, 1,orange)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,pink)
	addPixels(strip, 3,black)
	addPixels(strip, 1,pink)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,purple)
	addPixels(strip, 1,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 1,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 7,black)
	
	# 5
	addPixels(strip, 7,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 1,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 4,black)
	
	addPixels(strip, 1,blue)
	addPixels(strip, 3,black)
	addPixels(strip, 1,blue)
	
	addPixels(strip, 3,black)
	addPixels(strip, 1,white)
	addPixels(strip, 4,black)
	
	addPixels(strip, 1,yellow)
	addPixels(strip, 2,black)
	addPixels(strip, 2,yellow)
	
	addPixels(strip, 2,black)
	addPixels(strip, 1,orange)
	addPixels(strip, 3,black)
	addPixels(strip, 1,orange)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,pink)
	addPixels(strip, 3,black)
	addPixels(strip, 1,pink)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,purple)
	addPixels(strip, 1,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 1,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 7,black)
	
	# 6
	addPixels(strip, 7,black)
	addPixels(strip, 1,purple)
	addPixels(strip, 2,black)
	addPixels(strip, 2,purple)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,blue)
	addPixels(strip, 3,black)
	addPixels(strip, 1,blue)
	
	addPixels(strip, 1,black)
	addPixels(strip, 5,white)
	addPixels(strip, 2,black)
	
	addPixels(strip, 1,yellow)
	addPixels(strip, 3,black)
	addPixels(strip, 1,yellow)
	
	addPixels(strip, 2,black)
	addPixels(strip, 4,orange)
	addPixels(strip, 4,black)
	
	addPixels(strip, 3,pink)
	addPixels(strip, 4,black)
	
	addPixels(strip, 3,purple)
	addPixels(strip, 8,black)
	
	
	client.put_pixels(strip)

#returns title based on selection

def menuSel(sel):
	if(sel==0):
		extTitle()
	elif(sel == 1):
		sineTitle()
	elif(sel == 2):
		checksTitle()
	elif(sel == 3):
		weaveTitle()
	elif(sel == 4):
		heartTitle()
	elif(sel == 5):
		pipesTitle()
	elif(sel == 6):
		rainTitle()
	
	return True

