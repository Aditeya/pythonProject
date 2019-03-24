# Light each LED in sequence, and repeat.

import opc, time

numLEDs = 360
client = opc.Client('localhost:7890')

while True:
    for i in range(59, 0, -1):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i] = (255, 255, 255)
        client.put_pixels(pixels)
        time.sleep(0.01)
    for i in range(60, 119):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i] = (255, 255, 255)
        client.put_pixels(pixels)
        time.sleep(0.01)
    for i in range(179, 120, -1):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i] = (255, 255, 255)
        client.put_pixels(pixels)
        time.sleep(0.01)
    for i in range(180, 239):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i] = (255, 255, 255)
        client.put_pixels(pixels)
        time.sleep(0.01)
    for i in range(299, 240, -1):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i] = (255, 255, 255)
        client.put_pixels(pixels)
        time.sleep(0.01)
    for i in range(300, 359):
        pixels = [ (0,0,0) ] * numLEDs
        pixels[i] = (255, 255, 255)
        client.put_pixels(pixels)
        time.sleep(0.01)
