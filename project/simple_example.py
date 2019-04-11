#!/usr/bin/env python

import opc

#create list with 1 tuple, then make it 10 long
led_colour=[(255,255,0)]*360

print led_colour

#to use simulator
#client = opc.Client('localhost:7890')

#to use actual leds
client = opc.Client('192.168.2.1:7890')

client.put_pixels(led_colour)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
client.put_pixels(led_colour)
