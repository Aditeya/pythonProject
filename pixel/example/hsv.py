import colorsys
import opc
import time

client = opc.Client('localhost:7890')
s = 1
v = 1



for hue in range(360):
	rgb = colorsys.hsv_to_rgb(hue/360.0, s, v)
	leds=[rgb]*360
	client.put_pixels(leds)
	print(hue)
	print(rgb)
	s+=1
	v+=1
	time.sleep(1/30.0)
    
    

