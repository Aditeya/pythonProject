from ledutils import addPixels
import opc

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

ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)
client.put_pixels(strip)
client.put_pixels(strip)