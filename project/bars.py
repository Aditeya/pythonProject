from ledutils import addPixels
from time import sleep
from random import randint
import opc

strip = []
addPixels(strip, 300, (0,0,0))
addPixels(strip, 10, (255,0,0))
addPixels(strip, 50, (0,0,0))


client = opc.Client('localhost:7890')
client.put_pixels(strip)
sleep(0.025)

while True:
	i=randint(0,5)
	b = i
	while i >= 0:
		
		
		for j in range(10):
			strip[i*60 + j] = (255,0,0)
			
		client.put_pixels(strip)
		sleep(0.025)
		i-=1
	
	
	while i <= b:
		
		
		for j in range(10):
			strip[i*60 + j] = (0,0,0)
			
		client.put_pixels(strip)
		sleep(0.025)
		i+=1