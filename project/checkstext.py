from ledutils import addPixels
import opc

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

ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)
client.put_pixels(strip)
client.put_pixels(strip)