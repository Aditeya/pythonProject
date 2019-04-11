from ledutils import addPixels
import opc

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

ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)
client.put_pixels(strip)
client.put_pixels(strip)