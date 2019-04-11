import opc
import time
import random

# Each iteration has 15 pipes

def playPipes(iterations):
	ADDRESS = 'localhost:7890'
	client = opc.Client(ADDRESS)
	
	b = 0
	while b < iterations:
		strip = [(0,0,0)]*360
		client.put_pixels(strip)
		time.sleep(1/30.0)
		
		b+=1
		
		for i in range(15):
			start = True
			x = random.randint(0,59)
			y = random.randint(0,5)
			
			rColour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
			
			strip[y*60+x] = rColour
			client.put_pixels(strip)
			time.sleep(1/30.0)
			
			lastDirection = 0
			
			while start:
				growth = True
				growx = True
				
				while True:
					nextDirection = random.randint(1,4)
					
					if nextDirection != lastDirection:
						break;
				
				lastDirection = nextDirection
			
				if nextDirection == 1:
					if y-1 >= 0:
						y -= 1
						growth = random.randint(1,3)
						growx = False
				elif nextDirection == 3:
					if y+1 <= 5:
						y += 1
						growth = random.randint(1,3)
						growx = False
				elif nextDirection == 2:
					if x+1 <= 59:
						x += 1
						growth = random.randint(1,10)
						growx = True
				elif nextDirection == 4:
					if x-1 >= 0:
						y += 1
						growth = random.randint(1,10)
						growx = True
				
				for a in range(growth):
					if x < 0 or x > 59 or y < 0 or y > 5:
						start = False
						break
					
					strip[y*60+x] = rColour
					client.put_pixels(strip)
					time.sleep(1/30.0)
					
					if growx and nextDirection==2:
						x+=1
					elif growx and nextDirection==4:
						x-=1
					elif growx and nextDirection==1:
						y-=1
					elif growx and nextDirection==3:
						y+=1
						
	return strip