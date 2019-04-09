
import time
import opc
import threading


client = opc.Client('localhost:7890')

ledColor = [(0,0,0)]*360

BG = list(ledColor)

client.put_pixels(ledColor)

ledEnum = enumerate(ledColor)

def lineVer(amt):  #Creating the vertical line
	
	for y in range(0, 6):
		ledColor[(5-y)*60+15+amt] = (255,255,255)
		client.put_pixels(ledColor)
		time.sleep(0.075)
		
	return

def lineHor(amt):  #Creating the horizontal line
	
	for x in range(0, 60):
		ledColor[(amt+3)*60+x] = (255,255,255)
		client.put_pixels(ledColor)
		time.sleep(0.01)
		
	return
	
def lineVerEX(amt):   #Expanding the vertical line

	for y in range(0, 6):
		ledColor[(5-y)*60+15+amt] = (255,255,255)
	
	return
	
	
def lineHorEX(amt):   #Expanding the horizontal line

	for x in range(0, 60):
		ledColor[(4+amt)*60+x] = (255,255,255)

	return


def BGtransAnim():

	threading.Thread(target=lineVer, args=(0,)).start()
	time.sleep(0.005)
	threading.Thread(target=lineVer, args=(31,)).start()
	time.sleep(0.01)
	threading.Thread(target=lineHor, args=(0,)).start()
	time.sleep(0.5)
	
	threading.Thread(target=lineVer, args=(30,)).start()
	time.sleep(0.01)
	threading.Thread(target=lineHor, args=(-2,)).start()
	time.sleep(0.005)
	threading.Thread(target=lineVer, args=(9,)).start()
	time.sleep(0.75)
	
	threading.Thread(target=lineVer, args=(15,)).start()
	time.sleep(0.005)
	threading.Thread(target=lineVer, args=(21,)).start()
	time.sleep(0.01)
	threading.Thread(target=lineHor, args=(1,)).start()
	time.sleep(0.5)
	
	threading.Thread(target=lineVer, args=(-7,)).start()
	time.sleep(0.01)
	threading.Thread(target=lineHor, args=(-4,)).start()
	time.sleep(0.75)
	
	threading.Thread(target=lineVer, args=(27,)).start()
	time.sleep(0.01)
	threading.Thread(target=lineHor, args=(-3,)).start()
	time.sleep(0.75)
	
	threading.Thread(target=lineVer, args=(39,)).start()
	time.sleep(0.01)
	threading.Thread(target=lineHor, args=(-1,)).start()

BGtransAnim()